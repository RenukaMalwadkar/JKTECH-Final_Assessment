import sqlite3
def connection():
    con = sqlite3.connect("student.db")
    return con

# def create(con):
#     cur = con.cursor()
#     cur.execute("create table Students1(id integer,name text,age integer,course text);")
#     con.close()
#
#
# def insert(con):
#     cur = con.cursor()
#     cur.executescript("""
#     insert into Students1 values(1001,"john",21,"MCA");
#     insert into Students1 values(1002,"peter",22,"MSC");
#     insert into Students1 values(1003,"renuka",20,"MCA");
#     """)
#     con.commit()
#     con.close()
#
# def read(con):
#     cur = con.cursor()
#     cur.execute("select * from Students1")
#     data=cur.fetchall()
#     for d in data:
#         print(d)
#     con.close()

# def delete(con):
#     cur=con.cursor()
#     cur.execute("select * from Students1")
#     print("details before delete")
#     data=cur.fetchall()
#     for i in data:
#         print(i)
#     id=int(input("enter id to delete :"))
#     cur.execute('delete from Students1 where id = ?',(id,))
#     con.commit()
#     cur.execute("select * from Students1")
#     print("details after delete")
#     data=cur.fetchall()
#     for d in data:
#         print(d)
#     con.close()

def update(con):
    cur = con.cursor()
    cur.execute("select * from Students1")
    print("details before update")
    data = cur.fetchall()
    for i in data:
        print(i)
    id = int(input("enter id  :"))
    name=input("enter changed name to update : ")
    cur.execute('update Students1 set name=? where id = ?', (name,id))
    con.commit()
    cur.execute("select * from Students1")
    print("details after update")
    data = cur.fetchall()
    for d in data:
        print(d)
    con.close()1002

# con = connection()
# create(con)

# con = connection()
# insert(con)
# print("**********************display**********************")
# con = connection()
# read(con)
# print("**********************delete**********************")
# con = connection()
# delete(con)
print("**********************update**********************")
con=connection()
update(con)


