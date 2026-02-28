🚍 Transport Management System – OOP Explanation

Your system demonstrates the five core OOP principles:

Class & Object

Encapsulation

Inheritance

Polymorphism

Abstraction
(+ Composition / Association)

1️⃣ Class and Object
What is a Class?

A class is a blueprint.

Example:

class Vehicle:

It defines:

Attributes (data)

Methods (behavior)

What is an Object?

An object is an instance of a class.

minibus1 = MiniBus("B001", "ABC-123", 5000, route1.route_number)

Here:

MiniBus → class

minibus1 → object

2️⃣ Encapsulation

Encapsulation = binding data and methods together and protecting internal state.

In Vehicle:

self._status = "available"

The _status variable:

_ means "protected" (convention)

Should not be modified directly outside the class

Access through method:

def get_status(self):
    return self._status

✔ Data is controlled through methods.

3️⃣ Inheritance

Inheritance allows one class to reuse another class.

class Bus(Vehicle):

Meaning:

Bus IS-A Vehicle

Bus automatically gets:

vehicle_id

plate_number

capacity

start()

stop()

get_status()

Multi-Level Inheritance
class MiniBus(Bus):

MiniBus:

IS-A Bus

IS-A Vehicle

Hierarchy:

Vehicle
   ↑
  Bus
   ↑
MiniBus
4️⃣ Polymorphism

Polymorphism = same method name, different behavior.

In Bus:
def calculate_fare(self, distance):
    return f"Total fare: ${total_fare}"
In MiniBus (Method Overriding):
def calculate_fare(self, distance):
    return distance * 3.0

Same method name:

calculate_fare()

But different implementation.

That is Runtime Polymorphism.

5️⃣ Abstraction

Abstraction = hiding internal implementation details.

When you call:

minibus1.start()

You don’t care how _status changes internally.

You just use the behavior.

6️⃣ Composition / Association
Driver and Vehicle Relationship
self.assigned_vehicle = vehicle

Driver HAS-A Vehicle.

This is not inheritance.

It is:

Association (Driver uses Vehicle)

Route and Bus Relationship

You pass:

route1.route_number

This shows logical connection between:

Route

Bus

7️⃣ Static Method
class Maintenance:
    @staticmethod
    def perform_service(vehicle):

Static method:

Belongs to class

Does NOT use self

Can be called without creating object

Called like:

Maintenance.perform_service(minibus1)

Use case:
Utility functions related to class domain.

8️⃣ Class Variable
company_name = "National Transport Services"

This is shared among all vehicles.

Access:

Vehicle.company_name
🔎 Full OOP Concept Mapping
OOP Concept	Where Used
Class	Vehicle, Bus, Driver
Object	minibus1, driver1
Encapsulation	_status
Inheritance	Bus → Vehicle
Multi-level inheritance	MiniBus → Bus
Polymorphism	calculate_fare()
Abstraction	start(), stop()
Association	Driver HAS-A Vehicle
Static Method	Maintenance.perform_service()
Class Variable	company_name
🎯 Execution Flow Understanding

When you run:

print(driver1.assign_vehicle(minibus1))

Driver assigned vehicle

Returns string

print displays it

When you run:

print(minibus1.calculate_fare(10))

Python decides:

Object is MiniBus

So it uses MiniBus version of method

That is polymorphism

🧠 System Architecture (Simplified Diagram)
Vehicle
   ↑
  Bus
   ↑
MiniBus

Driver  ----->  Vehicle
Route   ----->  Bus
Maintenance (Utility Class)