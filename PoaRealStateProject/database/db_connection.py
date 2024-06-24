import sqlite3
from PoaRealStateProject.transformation.data_transformation import final_info_df

conn = sqlite3.connect('PoaRealStateProject\database\poa.db')
cursor = conn.cursor()
final_info_df.to_sql('base_table',conn,if_exists='replace',index=False)
with open('PoaRealStateProject\database\\table_creation.sql', 'r') as f:
    sql_script = f.read()
    cursor.executescript(sql_script)
    
conn.commit()
conn.close()
