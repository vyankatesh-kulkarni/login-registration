#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

print("<h2 align='center'> Sign up form</h2>")
form=''' <table align='center'>
        <form action ="register.py" method="POST">
        <tr>
         <td>Name:</td>
         <td><input type="text" name="name" required><td>
        </tr>
        <tr>
        <td> Email: </td>
        <td><input type="email" name="mail" required> </td>
        </tr>
        <tr>
         <td>Choose Username:</td>
         <td><input type="text" name="username" required> </td>
        </tr>
        <tr>
         <td>Choose Password: </td>
         <td><input type="password" name="pwd" required> </td>
        </tr>
        <tr> 
        <td><input type="submit" value="Sign up" required> </td>
        </tr>
        </form>
        </table>'''

print(form)
