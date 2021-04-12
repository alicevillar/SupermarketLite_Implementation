from source.people import People
import mysql.connector as mysql

my_db = mysql.connect(
  host="localhost",
  user="root",
  password="123",
  database="Supermarket_Database"
)

cursor = my_db.cursor()

class PersonDB:

    def adding(self, person):

        sql="INSERT INTO Person (Person_name, Phone, E_mail, Username, Password) values (%s,%s,%s,%s,%s)"
        val=person.name, person.phone, person.address, person.username, person.password
        cursor.execute(sql,val)
        my_db.commit() #mandando informaçÕes para o mysql

    def getting(self):
        sql = "SELECT * FROM Person"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    def getting_by_id(self):
        pass

    def deleting(self, person):
        pass

if __name__ == '__main__':
    person_1=People('Robert','1212','219988888', 'Avenue X','Rob',456)
    PersonDB().adding(person_1)

    #PersonDB().adding('Alice', 2222, 'aa @ aa.com', 'Ali', 321)
    PersonDB().getting()
