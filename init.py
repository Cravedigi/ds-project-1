import pandas as pd
import numpy as np
import uuid
import sqlite3

conn = sqlite3.connect('crm.db')
print("Database connected successfully")
cursor = conn.cursor()
name = input("Enter your name: ")
result = cursor.execute('SELECT * FROM bda WHERE name = \'{}\''.format(name)).fetchall()
if len(result) == 0:
  print("Wrong name")
else:
  print("Welcome", name, "to the CRM panel")


df = pd.read_csv('E:/teach/qbits/projects/progress/support_leads.csv')
print("Data loaded successfully")
print("Shape: ", df.shape)
print("........")

testrow = dict(df.iloc[0:1,:])
print(testrow)
