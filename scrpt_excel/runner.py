import sqlite3
import pandas as pd

filename = '../store.db'
conn = sqlite3.connect(filename)

wb = pd.read_excel('prodects.xlsx', sheet_name='Sheet1')
for sheet in wb:
    wb[sheet].to_sql(sheet, conn, index=False)
    conn.commit()
    conn.close()