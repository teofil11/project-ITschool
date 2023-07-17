import mysql.connector
from functions.write import wUpper


conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

class Employee():
    def __init__(self,fName,lName,company,idManager,email):
        self.fName = fName
        self.lName = lName
        self.company = company
        self.idManager = idManager
        self.email = email

        def registration(self):
            """
            Register an employee in the database.

            If there is an exception of type 'mysql.connector.errors.ProgrammingError', it means that the input contains non-letter characters.
            """
            try:
                if self.idManager == 'CEO':
                    cursor.execute(f"insert into employees values (null, '{wUpper(self.fName)}', '{wUpper(self.lName)}', '{wUpper(self.company)}', '{self.idManager}','{self.email}');")
                    conn.commit()
                    print('You have successfully registered')
                    
                cursor.execute('select * from employees')
                rows = cursor.fetchall()
                    
                for row in rows:
                    if self.idManager == str(row[0]):
                        if wUpper(self.company) == row[3]:
                            cursor.execute(f"insert into employees values (null, '{wUpper(self.fName)}', '{wUpper(self.lName)}', '{wUpper(self.company)}', '{self.idManager}','{self.email}');")   
                            conn.commit()
                            print('You have successfully registered')

            except mysql.connector.errors.ProgrammingError:
                print('Please enter only letters')

        registration(self)
