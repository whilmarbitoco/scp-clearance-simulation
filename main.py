import sqlite3, sys

conn = sqlite3.connect("scp.db")
c = conn.cursor()

def getscp(name, clearance):
    c.execute("SELECT name, security_level, description FROM scps WHERE name=?",(name,))
    rows = c.fetchone()
    if rows is not None:
        scpname, security_level, scpdescription = rows
        if clearance >= security_level:
            return [scpname, security_level, scpdescription]
        else:
            print("You have no clearance to view document")
    else:
        print("no documents found")


def personel(scp):
    global name
    c.execute("SELECT name, security_level FROM personel WHERE name=?", (name,))
    rows = c.fetchone()
    name, clearance = rows
    if getscp(scp, clearance):
        docs = getscp(scp, clearance)
        print(f"""
FILE: {docs[0]}
CLEARANCE LEVEL: {docs[1]}
DESCRIPTION: {docs[2]}
        """)
    
    
    
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
    name = input("NAME: ")
    password = input("PASSWORD: ")
    main(name, password)