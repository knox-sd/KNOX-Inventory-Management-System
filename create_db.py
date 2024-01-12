import sqlite3

def create_db():
    con = sqlite3.connect(database = r'knoxims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, gender text, contact text, email text, dob text, doj text, passw text, utype text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(sid TEXT PRIMARY KEY, name text, contact text, fax text, pobox text, email text, cpersion text, designa text, address text, descript text, bankname text, acname text, acnumber text, swift text, bankadd text, pterms text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS customer(cus_id TEXT PRIMARY KEY, cus_name text, cus_contact text, cus_fax text, cus_pobox text, cus_email text, cus_contpersion text, cus_designa text, cus_address text, cus_description text, cus_bankname text, cus_acname text, cus_acnumber text, cus_swift text, cus_bankadd text, cus_pterms text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS items(icode TEXT PRIMARY KEY, description text, division text, brand text, product text, category text, subcategory text, size text, model text, price text, barcode text, supplierID text, quantity INTEGER, status TEXT)")
    con.commit()

create_db()