\set ON_ERROR_STOP on
drop database if exists coredb;
create database coredb;
GRANT ALL PRIVILEGES ON DATABASE coredb to kobo;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
