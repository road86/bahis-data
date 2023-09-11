#! /bin/python3
from pipeline_scripts.prep_data import main as prep_data
from pipeline_scripts.prep_geojson import main as prep_geojson

prep_geojson()
prep_data()
