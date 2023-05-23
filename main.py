import requests
import json
import sqlite3
'''
saiti = requests.get('https://hp-api.onrender.com/')
print(saiti)
print(saiti.status_code)
print(saiti.headers)
print(saiti.headers['Content-Type'])
print(saiti.text)
'''

'''
url = "https://hp-api.onrender.com/api/spells"
response = requests.get(url)
with open('name.json', 'w') as file:
    json.dump(response.json(), file)
'''

'''
url = "https://hp-api.onrender.com/api/spells"
response = requests.get(url)
result = response.json()
# print(json.dumps(result, indent=4))
for num in range(len(result)):
    print(f"{result[num]['name']}")
'''


url = "https://hp-api.onrender.com/api/spells"
response = requests.get(url)
result = response.json()
conn = sqlite3.connect('spells.sqlite3')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS spells (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')
for num in range(len(result)):
    cursor.execute("INSERT INTO spells (id, name) VALUES (?, ?)", (num + 1, result[num]['name']))
conn.commit()
conn.close()





