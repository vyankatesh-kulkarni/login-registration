#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

import cgi
formdata=cgi.FieldStorage()

name=formdata.getvalue("name")
email=formdata.getvalue("mail")
username=formdata.getvalue("username")
password=formdata.getvalue("pwd")

import pymysql
db=pymysql.connect('localhost','root','','vyankatesh')
cursor=db.cursor()
query="INSERT INTO login(name,email,username,password) VALUES('{}','{}','{}','{}')".format(name,email,username,password)

cursor.execute(query)
db.commit()
print("You are registered ")
print("You can log in now !")
print("<a href='form.py'> login here</a>")
    
'''except:
    db.rollback()
    print("eror")'''


