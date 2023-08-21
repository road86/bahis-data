import logging
import pandas as pd
import sqlalchemy
import configparser
import os
import psycopg2
import shutil


os.makedirs('output',exist_ok=True)

bahis_config = configparser.ConfigParser()
bahis_config.read('bahis_creds_file.cnf')
which_db = 'bahis_credentials'

myBahisDB = sqlalchemy.engine.URL.create(drivername='postgresql+psycopg2',
                host = bahis_config[which_db]['host'],
                username = bahis_config[which_db]['user'],
                port = bahis_config[which_db]['port'],
                password = bahis_config[which_db]['password'],
                database = bahis_config[which_db]['database']
                )

bahis_connections = sqlalchemy.create_engine(url=myBahisDB, echo=True)

conn = bahis_connections.connect()

# table named 'contacts' will be returned as a dataframe.
save_tables = ['bahis_species_table',
               'bahis_diagnosis_table',
               'bahis_diagnosis_table',
               'bahis_patient_registrydyncsv_live_table',
               'geo_cluster']

for s_table in save_tables:
    s_dat = pd.read_sql_table(s_table, bahis_connections, schema='core')
    s_dat.to_csv(f'output/newbahis_{s_table}.csv', index=False)

conn.close()
bahis_connections.dispose()

#HACK
# pnadas read_sql_table do not correctly reads json columns from postgresql. Temporarily we will just use the file exported manually for old bahis.
shutil.copyfile('input/oldbahis_forms_data.csv', 'output/oldbahis_forms_data.csv')
shutil.copyfile('input/oldbahis_fao_species.csv', 'output/oldbahis_fao_species.csv')
