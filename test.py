# saved_admin='Mithun'
# saved_admin_password='1234'
# def validate(admin,password):
#   if(admin!=saved_admin):
#     str=input("Incorrect username \n  please enter valid username")
#     validAdmin(str,password)
#     elif(password!=saved_admin_password):
#       str=input("Incorred password \n Please enter valid password")
#       validPassword(admin,str)
#       else:
#         print("Valid successfully")
# print("Welcome")
# print(1.Admin 2.User)
# choice=int(input("Enter the "))


import mysql.connector

connection  = mysql.connector.connect(database='library',password='Aspire@123',host='localhost',user='root',buffered = True)
cursor = connection.cursor()


print("1.Admin\n2.User")
value = int(input("Enter your choice:"))
if (value==1):
  admin_name = input("ENter the admin name:")
  admin_password = input("enter  the password:")
  query = f"select count(*) from admin where name = '{admin_name}' and password = '{admin_password}' "
  cursor.execute(query)
  connection.commit()
  count = cursor.fetchone()
  if (count[0]):
    print("Admiin found")


  else:
    print("Admin not found")
  cursor.close()

else:
  user_name=input("Enter your Username")
  user_password=input("Enter the password")
  query=f"select count(*) from user where name='{user_name}' and password ='{user_password}'"
  cursor.execute(query)
  connection.commit()
  count=cursor.fetchone()
  if(count[0]):
    print("user found")

   
    cursor.close()

