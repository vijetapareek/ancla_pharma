# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import sqlite3

con = sqlite3.connect(r"D:\workspace\finaltask\anclatech\db.sqlite3")

# Load the data into a DataFrame
# surveys_df = pd.read_sql_query("SELECT * from auth_permission", con)

# Select only data for 2002
product_start_end_df = pd.read_csv(r"D:\workspace\finaltask\anclatech\pharmapp\static\pharmapp\data\product.csv")
event_start_end_df = pd.read_csv(r"D:\workspace\finaltask\anclatech\pharmapp\static\pharmapp\data\event.csv")
# Write the new DataFrame to a new SQLite table
product_start_end_df.to_sql("product", con, if_exists="replace")
event_start_end_df.to_sql("event", con, if_exists="replace")


con.close()