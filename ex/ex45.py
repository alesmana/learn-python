## Animal is-a object 
class Animal(object):
    pass
    
## is-a
class Dog(animal):
    def __init__(self, name):
        ## has-a
        self.name = name
        
## is-a
class Cat(animal):
    def __init__(self, name):
        ## has-a
        self.name =name
        
## Person is-a object
class Person(object):
    def __init__(self, name):
        ## has-a
        self.name = name
        
        ## Person has-a pet 
        self.pet = None
        
## is-a
class Employee(person):
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

## mary has-a pet called satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()