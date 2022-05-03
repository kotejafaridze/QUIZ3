import requests
import json
import sqlite3


#es api gibrunebs simgeris lyrics artistis da simgeris saxelis mixedvit.
#didi asoti unda daiwkos saxeli da simgeris saxeli

artist = input("შეიყვანეთ არტისტის სახელი პირველი დიდი ასოთი მაგალითად Imagine Dragons")
title = input("შეიყვანეთ სიმღერის სახელი მაგალითად Believer")

res = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')

#PIRVELI DAVALEBASHI MOTXOVNILI 3 funqcia.
# headers = res.headers
# st_code = res.status_code
# print(headers)
# print(st_code)

result = json.loads(res.text)
print(json.dumps(result, indent=4))# es aris meore daveleba, tumca radgan dictionaryshi mxolod erti elementia,>>
# ar gamodis sxvanairi struqturit dabechdva.


lyrics = result.get('lyrics')
print(lyrics)#ese ibechdeba kvelaze kargi struqturit. Mesame punqti.



con = sqlite3.connect("songs.sqlite")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Songs
    ( id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist VARCHAR(40),
    title VARCHAR(40),
    json VARCHAR(100)
    )  
''')

if res.status_code == 200:
    cursor.execute('INSERT INTO songs (artist, title, json) VALUES (?, ?, ?)', (artist, title, res.url))

con.commit()

con.close()
