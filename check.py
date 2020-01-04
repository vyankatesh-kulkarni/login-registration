#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

import cgi
formdata=cgi.FieldStorage()

username=formdata.getvalue("username")
password=formdata.getvalue("pwd")

import pymysql
db=pymysql.connect('localhost','root','','vyankatesh')
cursor=db.cursor()
query="SELECT * FROM login WHERE username='{}'".format(username)
try:
    cursor.execute(query)
    data=cursor.fetchall()
    pwd=data[0][4]
    unm=data[0][3]
except:
   print("<h3>Sorry! you have entered invalid credentials</h3>")
    
if unm==username:
    if pwd== password:
        print("<h3>You have loged in sucessfully !!!!</h3>")
    else:
        print("<h3>You have entered wrong password</3>")
'''else:
    print("invalid credentials")'''


    
#o/p => ((10, 'amit', 'amit@m.com', 'amit', 'ami22'),)
