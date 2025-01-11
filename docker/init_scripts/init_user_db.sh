#!/bin/bash
set -e  # Exit immediately if any command fails

# Variables from the environment
POSTGRES_USER=${POSTGRES_USER:-postgres}  # Default to 'postgres' if POSTGRES_USER is not defined
POSTGRES_DB=${POSTGRES_DB:-network_db}    # Default to 'network_db' if POSTGRES_DB is not defined

# Create the database user if it doesn't exist
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname=postgres <<-EOSQL
DO
\$do\$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '${POSTGRES_USER}') THEN
      CREATE ROLE ${POSTGRES_USER} LOGIN PASSWORD '${POSTGRES_PASSWORD}';
   END IF;
END
\$do\$;
EOSQL

# Create the database if it doesn't exist and grant ownership
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname=postgres <<-EOSQL
DO
\$do\$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = '${POSTGRES_DB}') THEN
      CREATE DATABASE ${POSTGRES_DB} OWNER ${POSTGRES_USER};
   END IF;
END
\$do\$;
EOSQL
