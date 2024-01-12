import sqlite3

def create_db():
    con = sqlite3.connect(database = r'knoxims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, gender text, contact text, email text, dob text, doj text, passw text, utype text, address text, salary text)")
    con.commit()

create_db()