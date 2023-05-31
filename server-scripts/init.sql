\set ON_ERROR_STOP on
drop database if exists coredb;
drop database if exists bahistot;
create database coredb;
create database bahistot;
GRANT ALL PRIVILEGES ON DATABASE coredb to kobo;
GRANT ALL PRIVILEGES ON DATABASE bahistot to kobo;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
