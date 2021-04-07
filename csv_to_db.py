import sqlite3
import csv


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

reader = csv.reader(open('ingredients.csv', encoding='utf-8'))
sql = "INSERT INTO recipes_ingredient (title, unit) VALUES (?, ?);"
for row in reader:
    cur.execute(f"{sql}", row)
conn.commit()
conn.close()
