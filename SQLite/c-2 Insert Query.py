import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''  
    
    insert into student(st_name,st_class,st_email) VALUES('adi','SWE','adiroy0711@gmail.com')
'''
conn.execute(ins)
conn.commit() # new data insert delete hole commit keyword use korbo.
conn.execute(ins)
conn.commit()
conn.close()

