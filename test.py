import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import os
import re
import psycopg2

##Creating engine to connect to sql database
#create_engine(dialect+driver://username:password@host:port/database)
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/coredb")
connection = engine.connect()

##Reading Tables
#Reading a table using sqlalchemy
metadata = sqlalchemy.MetaData()
data = connection.execute(text('select * from core.bahis_avian_influenza_investigate_p2_table')).fetchall()
print(data)

#Reading a table using pandas
df = pd.read_sql_table("bahis_avian_influenza_investigate_p2_table", con = connection, schema= "core")
print(df)

df.to_csv("output/AI_Investigation.csv")