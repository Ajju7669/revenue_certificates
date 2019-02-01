import sqlite3
def Create_Table():
	connection=sqlite3.connect("login.db")
	"""connection.execute("Create table officers(Username text not null,password text,option text)")"""
	"""connection.execute("insert into officers values ('operator','operator@123','System Operator')")
	connection.commit()"""
	connection.execute("alter table officers rename column password to Password")
	result=connection.execute("select * from officers")
	for i in result:
		print("Username:",i[0])
		print("password:",i[1])
		print("Designation:",i[2])

	connection.close()
Create_Table()
