import logging
import pandas as pd
import sqlalchemy
import configparser
import os
import psycopg2
import shutil
import glob


os.makedirs("output", exist_ok=True)

bahis_config = configparser.ConfigParser()
bahis_config.read("bahis_creds_file.cnf")
which_db = "bahis_credentials"

myBahisDB = sqlalchemy.engine.URL.create(
    drivername="postgresql+psycopg2",
    host=bahis_config[which_db]["host"],
    username=bahis_config[which_db]["user"],
    port=bahis_config[which_db]["port"],
    password=bahis_config[which_db]["password"],
    database=bahis_config[which_db]["database"],
)

bahis_connections = sqlalchemy.create_engine(url=myBahisDB, echo=True)

conn = bahis_connections.connect()

# table named 'contacts' will be returned as a dataframe.
save_tables = [
    "bahis_species_table",
    "bahis_diagnosis_table",
    "bahis_diagnosis_table",
    "bahis_patient_registrydyncsv_live_table",
    "geo_cluster",
    "bahis_farm_assessment_p2_table",
    "farm_assessment_logger",
    "bahis_avian_influenza_investigate_p2_table",
    "bahis_disease_investigation_p2_table",
    "bahis_participatory_livestock_assessment_table",
    "bahis_medicine_table",
]


for s_table in save_tables:
    s_dat = pd.read_sql_table(s_table, bahis_connections, schema="core")
    s_dat.to_csv(f"output/newbahis_{s_table}.csv", index=False)

conn.close()
bahis_connections.dispose()

# HACK
# pandas read_sql_table do not correctly reads json columns from postgresql. Temporarily we will just use the file exported manually for old bahis.
shutil.copyfile("input/Diseaselist.csv", "output/Diseaselist.csv")  # the google doc of disease list
shutil.copyfile(glob.glob("input/oldbahis_forms_data*.csv")[-1], "output/oldbahis_forms_data.csv")
shutil.copyfile(glob.glob("input/oldbahis_fao_species*.csv")[-1], "output/oldbahis_fao_species.csv")
