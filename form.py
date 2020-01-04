#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

print("<h2 align='center'> Login Here</h2>")
form='''<table align="center">
        <form action ="check.py" method="POST">
         <tr>
         <td> Username:</td>
         <td><input type="text" name="username" placeholder="username" autocomplete="off" required> </td>
         </tr> 
         <tr> <td> </td></tr>
         <tr>
          <td>Password:</td>
          <td><input type="password" name="pwd"  placeholder="password" autocomplete="off" required> </td>
         </tr>
         <tr> <td> </td></tr>
         <tr>
          <td colspan='2'><input type="submit" value="Log in now" required> </td>
         </tr>
         </form>
         <tr> <td> </td></tr>
         <tr> <td> </td></tr>
         <tr>
         <td> Not a member yet </td>
         <td> <a href='signup.py'> Sign up here </a> </td>
         </tr>
         </table>'''
          
print(form)

