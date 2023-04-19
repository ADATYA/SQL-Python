import sqlite3

# create a database
conn=sqlite3.connect("sqlite.db")

# create a tabble
conn.execute('''
        Create table student(
            st_id INT AUTO _INCREMENT PRIMARY KEY,
            st_name VARCHAR(50),
            st_class VARCHAR(10),
            st_email VARCHAR(50)
            
        )

''')    
conn.close()