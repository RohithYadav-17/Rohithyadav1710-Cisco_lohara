class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!
dog2 = Dog("charlie", 4)
print(dog2.description())  # Output: Buddy is 3 years old.
print(dog2.speak("boww!"))  # Output: Buddy says Woof!
dog3= Dog("chimtu", 2)
print(dog3.description())  # Output: Buddy is 3 years old.
print(dog3.speak("chimtu hai bhAAi"))  # Output: Buddy says Woof!
dogs=[dog1,dog2,dog3]
from functools import reduce
#reduce syntax
#reduce(<func>,iterable,init_value)
ages_sum=reduce((lambda s,dog:s+dog.age),dogs,0)
print(ages_sum)


