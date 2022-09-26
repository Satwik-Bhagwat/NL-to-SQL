import os
import json
import sqlite3


table_info = {}


for db in os.listdir('database'):
	for file in os.listdir(os.path.join('database', db)):
		if 'sqlite' in file:
			conn = sqlite3.connect(os.path.join('database', db, file))
			cursor = conn.cursor()

			tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
			table_keys = {}

			for table in tables:
				cols = cursor.execute("PRAGMA table_info({})".format(table[0])).fetchall()
				table_keys[table[0]] = [col[1] for col in cols]
			
			table_info[db] = table_keys

with open('tableInfo.json', 'w') as file:
    json.dump(table_info, file, indent=4)


# remove 0KB sqlite files created in working directory
for file in os.listdir():
	if 'sqlite' in file:
		os.remove(file)