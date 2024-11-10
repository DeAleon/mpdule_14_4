import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')

# for i in range(1, 5):
#     cursor.execute(f'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (f'Продукт{i}', f'Описание{i}', i * 100))

connection.commit()
connection.close()

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_product =  cursor.fetchall()
    connection.commit()
    connection.close()
    return all_product


