#!/bin/bash

# Make scripts in init-scripts executable
chmod +x init_scripts/*.sh

# Bring up the Docker Compose project
docker-compose -p social-network up
