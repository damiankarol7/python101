#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną w pamięci RAM
con = sqlite3.connect(':memory:')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel
cur.executescript("""
    DROP TABLE IF EXISTS klasa;
    CREATE TABLE IF NOT EXISTS klasa (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    );
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# wstawiamy dane uczniów
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

# wykonujemy zapytanie SQL, które pobierze id klasy "1A" z tabeli "klasa".
cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
klasa_id = cur.fetchone()[0]

# wstawiamy dane uczniów
cur.execute('INSERT INTO uczen VALUES(?,?,?,?)',
            (None, 'Tomasz', 'Nowak', klasa_id))
cur.execute('INSERT INTO uczen VALUES(?,?,?,?)',
            (None, 'Adam', 'Kowalski', klasa_id))

# zatwierdzamy zmiany w bazie
con.commit()
