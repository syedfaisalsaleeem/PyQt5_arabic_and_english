from objectbox.model import *
import objectbox
@Entity(id=1, uid=1)
class Person():
    id = Id(id=1, uid=1001)
    #first_name = Property(str, id=2, uid=1002)
    #last_name = Property(str, id=3, uid=1003)
    first_name=list()

# from mypackage.model import Person

# Configure ObjectBox: should be done only once in the whole program and the "ob" variable should be kept around
model = objectbox.Model()
model.entity(Person, last_property_id=objectbox.model.IdUid(3, 1003))
model.last_entity_id = objectbox.model.IdUid(1, 1)
ob = objectbox.Builder().model(model).directory("db").build()

# Open the box of "Person" entity. This can be called many times but you can also pass the variable around
box = objectbox.Box(ob, Person)
 
id = box.put(Person())  # Create
person = box.get(id)  # Read
#print(person)
#person.last_name = "Black"
person.first_name.append("faisal")
box.put(person)       # Update
#box.remove(person)    # Delete
print(person.first_name)