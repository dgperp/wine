#!/bin/bash

MODULES=${MODULES:-}
DATABASES=$(sudo docker exec -i db psql -U odoo -d postgres -t -c "SELECT string_agg(datname, ',') FROM pg_database WHERE datistemplate = false AND datname != 'postgres';")
DATABASES=$(echo $DATABASES | tr -d ' \n' | sed 's/^,//;s/,$//')
echo "Available databases: $DATABASES"
sudo docker-compose stop
sudo DB_PASSWORD=${DB_PASSWORD:-} DATABASES=$DATABASES MODULES=$MODULES docker-compose up -d
