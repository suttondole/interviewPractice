##start with class definition
##keyword "pass" allows you to leave things empty without throwing an error

class Dog:
    
    ##all classes must start with "__init__" function, this is where we
    ##define attributes (i.e. variables to be inherited)
    ##we can also define attributes that every instance of the class will
    ##have. Species is an example of this, as it is not under the init
    
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ##in order to access the values in the shell (or in the buffer) we first
    ##have to create an object (in this case we write "Buddy = Dog("Buddy", 4)")
    ##once we create the object, we access its' attributes using "Buddy.name" which
    ##prints the name. We can also change its' values by saying "Buddy.age = 8". Note
    ##we also can change class attributes the same way.

    ##same way in C++, we can write functions for classes. Similarly, these functions
    ##can only be accessed by objects of the class type. To use, we do the same as
    ##accessing attributes. (i.e. Buddy.description())

    ##def description(self):
    ##    return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    ##similar to the __init__ function, most classes have a __str__() function which
    ##prints out important info about the class. Notice the function description() does
    ##pretty much that, but we would want to use the __str__() function so we comment
    ##out the description(). With the __str__() function, all we have to do is say
    ##print(Buddy). This calls the __str__() function. Both the str and init function
    ##are called dunder methods because they begin and end with double underscores.
    ##There are other dunder methods, but we won't cover that here.

    def __str__(self):
        return f"{self.name} is {self.age} years old"



