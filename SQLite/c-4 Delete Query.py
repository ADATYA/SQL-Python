import sqlite3
conn=sqlite3.connect("sqlite.db")

st_id=input("Enter the student Name : ")
conn.execute("DELEAT FROM student where st_name="+st_name)
conn.commit()
conn.close()