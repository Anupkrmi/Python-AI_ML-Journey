print("Object Oriented Programming in Python")
print("Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. Python supports OOP and allows you to create classes, instantiate objects, and define methods and attributes.")
print("In Python, a class is defined using the 'class' keyword, and an object is an instance of a class. Classes can have attributes (variables) and methods (functions) that define the behavior of the objects created from the class.")

print("The '__init__' method is a special method in Python classes that is called when an object is instantiated. It is used to initialize the attributes of the object.")
print("Self is a reference to the current instance of the class and is used to access variables and methods associated with the current object.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
print("The 'Person' class has been defined with an '__init__' method to initialize the name and age attributes, and a 'greet' method to return a greeting message.")
person1 = Person("Alice", 30)
print(person1.greet())
person2 = Person("Bob", 25)
print(person2.greet())

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
print("The 'Car' class has been defined with an '__init__' method to initialize the make, model, and year attributes, and a 'description' method to return a description of the car.")
car1 = Car("Toyota", "Camry", 2020)
print(car1.description())
car2 = Car("Honda", "Civic", 2019)
print(car2.description())

print("Inheritance is a feature of OOP that allows a class to inherit attributes and methods from another class. The class that inherits is called the child class, and the class being inherited from is called the parent class.")
print("In Python, inheritance is implemented by passing the parent class as a parameter to the child class.")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

print("The 'Animal' class is a parent class with a 'speak' method that raises a NotImplementedError. The 'Dog', 'Cat', and 'Cow' classes are child classes that inherit from the 'Animal' class and implement the 'speak' method.")
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")
print(dog.speak())
print(cat.speak())
print(cow.speak())

print("Polymorphism is a feature of OOP that allows methods to do different things based on the object it is acting upon. In Python, polymorphism can be achieved through method overriding and duck typing.")

def animal_sound(animal):
    print(animal.speak())

print("The 'animal_sound' function demonstrates polymorphism by calling the 'speak' method on different animal objects. Each object responds according to its own implementation of the 'speak' method.")
animal_sound(dog)
animal_sound(cat)
animal_sound(cow)

print("Private and Public Data in classes")

