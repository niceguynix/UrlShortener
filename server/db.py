import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, u_name TEXT, pass TEXT, o_url TEXT, n_url TEXT)')
conn.close()
