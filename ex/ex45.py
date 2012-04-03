## Animal is-a object 
class Animal(object):
    pass
    
## is-a
class Dog(Animal):
    def __init__(self, name):
        ## has-a
        self.name = name
        
## is-a
class Cat(Animal):
    def __init__(self, name):
        ## has-a
        self.name =name
        
## Person is-a object
class Person(object):
    def __init__(self, name):
        ## has-a
        self.name = name
        
        ## Person has-a pet 
        self.pets = []
        
## is-a
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? initializing name?
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary
        
## is-a   
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass
    

## is-a
class Halibut(Fish):
    pass
    
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-many pet one if it is called satan
mary.pets.append(satan)

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-many pet one if it is called rover
frank.pets.append(rover)

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()