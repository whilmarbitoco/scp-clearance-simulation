import sqlite3, sys

conn = sqlite3.connect("bin/db/scp.db")
c = conn.cursor()

def getscp(name, clearance):
    c.execute("SELECT * FROM scps WHERE name=?", (name,))
    rows = c.fetchall()
    row = rows
    scpname = row[0][0]
    securitylevel = row[0][1]
    scpdescription = row[0][2]
    if int(clearance) >= int(securitylevel):
      return [scpname, securitylevel, scpdescription]
    


def personel(scp):
    global name
    c.execute("SELECT * FROM personel WHERE name=?", (name,))
    rows = c.fetchall()
    row = rows
    clearancelevel = row[0][2]
    check = getscp(scp, clearancelevel)
    if check:
        print(f"""
Filename: {check[0]}
Security Clearance Level: {check[1]}
Description: {check[2]}
        """)
    else:
      print("You no clearance for this information.")
    
    
def login(username, password):
    c.execute('''
    SELECT * FROM personel
    WHERE name=? AND password=?
    ''', (username, password))
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False
    
    
def main(name, password):
    if login(name, password):
        print("welcome to the scp foundation")
        while login(name, password):
            print ("""
1. View Scp information
2. Logout
            """)
            prompt = input(">> ")
            if prompt == "1":
                sname = input("scp filename: ")
                personel(sname)
            elif prompt == "2":
                sys.exit()
            else:
                print("not found")
   
   
while True:
    name = input("Name: ")
    password = input("Password: ")
    main(name, password)