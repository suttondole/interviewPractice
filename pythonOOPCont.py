##this doc serves as an extension of basic class declaration and execution
##we start off by introducing subclasses (think of it as parent/child.) using the same
##class as the dog class in pythonOOPtutorial.py, though we will add some stuff


class Dog:
    
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
##here we create three more classes for specific breed of dogs. Note that we must pass
##"Dog" as an argument so that the interpreter knows it is a subclass of Dog, therefore
##inheriting all of its attributes. now we can say Buddy = Dachshund("Buddy", 9).
##we can use function isinstance(name of object, class we are wanting to know if) to
##determine if an object is an instance. Returns true or false


class JackRussellTerrier(Dog):

    ##since each dog has a different sounding bark, we want to create a speak function in
    ##each species type. Note we still have the speak function in the Dog class.
    ##doing this, the species class overrides the dog class. Doing so provides a default
    ##value for each species.
    ##tying this all together, we create a dog of specific breed by
    ##miles = JackRussellTerrier("Miles", 4)
    ##if we want to use the default sound for each breed, we use miles.speak()
    ##we can also use the speak() method found in the Dog class by miles.speak("Grrr")
    ##note the difference is in what we pass as the parameters
    
    ##def speak(self, sound = "Arf"):
        ##return f"{self.name} says {sound}"

    ##sometimes this method is okay, although in this instance we dont want the format of
    ##the JackRussellTerrier's speak() function to be different than that of the Dog's
    ##speak function if we were to make changes. (in other words if we change the format
    ##of one, it won't be the same as the other, we would have to manually change each)
    ##to get around this, we introduce the super() function. This allows each species to
    ##be with out a doubt the same as its' parent class.

    def speak(self, sound = "Arf"):
        return super().speak(sound)

    ##note the difference. We essentially tell the interpreter that the contents of the
    ##species' speak are the same as its' parent class, though now we need to match the
    ##way the function is called in Dog by passing its' "sound" as a parameter.

class Dachshund(Dog):
    
    pass

class Bulldog(Dog):
    
    pass
