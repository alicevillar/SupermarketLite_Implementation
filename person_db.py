from people import People

class PersonDB:
    def get_all(self):
        return self.people

    def add_person(self,person):
        self.people.append(person)

    def get_by_id(self,id):
        for person in self.people:
            if person.id==id:
                print("Achou :)")
                return person
            else:
                print("Try again")
        return None




    def __init__(self):

        self.people = [
            People("Ann", 1642299, 988093939, "AvenidaXXX", "Carolzinha", "Carol2345"),
            People("Ben", 2642299, 988093939, "AvenidaXXX", "Carolzinha", "Carol2345"),
            People("Ci", 3642299, 988093939, "AvenidaXXX", "Carolzinha", "Carol2345"),
            People("Di", 4642299, 988093939, "AvenidaXXX", "Carolzinha", "Carol2345"),
            People("Ele", 5642299, 988093939, "AvenidaXXX", "Carolzinha", "Carol2345"),
        ]