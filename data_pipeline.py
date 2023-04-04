import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import sys
import os
import re
import psycopg2
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="INFO")

#Creating engine to connect to sql database
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/coredb")
logger.info("Engine created")

connection = engine.connect()
logger.info("Connection established")

metadata = sqlalchemy.MetaData()

#Reading Tables
##Reading a table using pandas
df = pd.read_sql_table("bahis_avian_influenza_investigate_p2_table", con = connection, schema= "core")
logger.info("Avian Influenza Table loaded")

print(df)

df_cleaned = df.drop(df[(df["basic_info_village"] == "test") |(df["basic_info_village"] == "tesat") | (df["basic_info_village"] == "dsfdsf")].index)
logger.info("Test data removed")


df.to_csv("output/AI_Investigation.csv")
logger.info("Exported as csv")

df_cleaned.to_csv("output/AI_Investigation_cleaned.csv")
logger.info("cleaned database exported as csv")