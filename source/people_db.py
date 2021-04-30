from people import People
import mysql.connector as mysql


my_db = mysql.connect(
  host="localhost",
  user="root",
  password="123",
  database="Supermarket_Database"
)

cursor = my_db.cursor()

# 1 - Creating the database
def create_database():
    sql="CREATE DATABASE IF NOT EXISTS Supermarket_Database"
    cursor.execute(sql)
    sql="USE Supermarket_Database"
    cursor.execute(sql)

# 2 - Creating table for person
def create_table():
    sql="CREATE TABLE IF NOT EXISTS person(" \
        "person_cod INT AUTO_INCREMENT PRIMARY KEY," \
        "person_name varchar (300) not null," \
        "phone INT not null " \
        "email varchar(255) not null," \
        "username varchar(255) not null," \
        "password varchar (255) not null)"
    cursor.execute(sql)

# 3 - Creating new person
def create_new_person(self, person):

    sql="INSERT INTO Person (Person_name, Phone, E_mail, Username, Password) values (%s,%s,%s,%s,%s)"
    val=(person.name, person.phone, person.address, person.username, person.password)
    cursor.execute(sql,val)
    my_db.commit() #mandando informaçÕes para o mysql


# 4 - Getting all from the table person
def get_all_persons():
    sql = "SELECT * FROM Person"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

# 5 - Getting person by ID
def getting_person_by_code(person_cod):
    sql= f"SELECT * FROM person WHERE person_code={person_cod}"
    cursor.execute(sql)
    result=cursor.fetchone()
    return result

# 6 - Updating person by code
def updating_person_by_code(updating_person):
    sql= f"UPDATE person SET person_name='{updating_person.person_name}'," \
         f"phone='{updating_person.phone}', " \
         f"email='{updating_person.email}'," \
         f"username='{updating_person.username}'," \
         f"password='{updating_person.password}'" \
         f"WHERE person_code={updating_person.person_cod}"
    cursor.execute(sql)
    #because I'm changing a table I must commit to save it:
    my_db.commit()

# 6 - Deleting person by code
def deleting_person_by_code(person_cod):
    sql=f"DELETE from person WHERE person_cod='{person_cod}'"
    cursor.execute(sql)
    #because I'm changing a table I must commit to save it:
    my_db.commit()

#Creating a database and a table:
create_database()
create_table()

#Creating person_1:
person_1=("Ali",21988093903,"ali@alice.com.br","Li","121212")
#create_new_person(person_1)

creating_list_with_everyone=get_all_persons()
print(creating_list_with_everyone)







#if __name__ == '__main__':
    #person_1=People('Robert','1212','219988888', 'Avenue X','Rob',456)
    #PersonDB().adding(person_1)

    #PersonDB().adding('Alice', 2222, 'aa @ aa.com', 'Ali', 321)
    #PersonDB().getting()
