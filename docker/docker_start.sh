#!/bin/bash

chmod +x init_scripts/*.sh

docker-compose -p social-network up --build
