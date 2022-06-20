import sqlite3

dbh = sqlite3.connect('excelr.db')
c = dbh.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empid REAL, ename REAL, tech REAL)") # data types:txt, real

# create_table()

def load_data():
    id = int(input("Empid: "))
    name = input("name: ")
    skill = input("Tech: ")
    c.execute("INSERT INTO employee VALUES(?, ?, ?)",(id,name,skill))

def update_data():
    c.execute("UPDATE employee SET tech = 'Web Tech' WHERE Tech='Testing'")

# update_data()
def delete_data():
    c.execute("DELETE FROM employee WHERE Tech = 'AIML'")

# delete_data()

def read_data():
    c.execute("SELECT * FROM employee")
    # print(c.fetchone())
    # print(c.fetchmany(2))
    for i in c.fetchall():
        print(i[1].upper() + " ===> " + i[2].upper())

read_data()

# for x in range(2):
#     load_data()
dbh.commit()
c.close()
dbh.close()
