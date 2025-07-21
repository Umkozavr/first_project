from dotenv.main import DotEnv

import creds
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWD'),
    host=creds.host,
    port=creds.port,
    database=creds.database
)

cursor = db.cursor(dictionary=True)

select_query = '''
    SELECT * FROM students 
    WHERE name = 'George' 
    AND second_name = 'Washington' 
'''
cursor.execute(select_query)
print(cursor.fetchone())
db.commit()
db.close()
