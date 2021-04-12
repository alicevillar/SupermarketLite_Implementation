# SUPERMARKET_LITE

# 7 CLASSES:
# People - name,id,phone,address,username,password
# Staff - salary, position
# Products - name, id, category
# Customers - purchaseHistory
# LoyatySchemes - id, total
# OnlineOrders- id
# Payment - id

from source.database.people_db import PersonDB

#Testing code:

#Creating a person and then one employee:
#person1 = People("Carol", 1642299, 988093939, "AvenidaXXX", "Carol", "Carol2345")
#print(person1.name)

#creating employee:
#employee1 = Staff(person1.name, person1.id, person1.phone, person1.address, person1.username, person1.password, 20000,"CE0")
#print(employee1.salary)

#creating person_db:
person_db=PersonDB()
#person_db.adding(person1)

#for person in person_db.get_all():
    #print(person.name)


person_db.getting(1)
