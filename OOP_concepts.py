#OOP Concepts
print('OOP Concepts')

print('\nClasses , Object')

print('defining class SampleClass')
class SampleClass():
    pass

print('\ncreating instance/object')
obj = SampleClass()
print(f'object obj of type {type(obj)} created')

print('\nExample 2....dog class with breed, color as attributes')
class dog():

    #class object attribute -  these are same for any instance of class
    species = 'Mammels'

    def __init__(self, color, breed,name,spots):   #parameters
        #attribute
        self.color = color
        self.breed = breed
        self.name = name
        #expect boolean
        self.spots = spots


    #methods, with self and outside arguments
    def bark(self,number):
        print(f'woooooffff!!! my name is {self.name} and i am number {number} :)')

#1my_dog = dog(mycolor = 'white', mybreed = 'Labrador')

#2
my_dog = dog('white', 'Labrador','Tommy',True)

print(f"my {my_dog.breed} is {my_dog.color} in color with {'spots' if my_dog.spots else 'no spots'}")
print(f'dogs are {my_dog.species}')
my_dog.bark(1)


#3
print('\nexample 3 ...class Circle')

class Circle():
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = Circle.pi*(radius**2)

    #circumeerence
    def calc_circumference(self):
        return 2*self.pi*self.radius

c = Circle(30)
print(f'Circumference is {c.calc_circumference()}')
print(f'Area is {c.area}')


print('\nInheritance')

print('Example 4...Inheritance using base class animal and other derivedclasses')

#base class
class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('I am eating')

#derived class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    #overriding base class method
    def who_am_i(self):
        print('i am a dog')

    def eat(self):
        print('i ma eating biscuit')
    #own special methods
    def bark(self):
        print('wooooffff!!!!')


mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()


print('\nPolymorphism')

print('Example 4...Polymorphism using cat and dog class')

class dogg():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woooffff!!'

class cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!!'


tommy = dogg('Tommy')
sylvester = cat('Sylvester')

print(tommy.speak())
print(sylvester.speak())

#abstract class for the polymorphism

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')


class dogg(Animal):

    def speak(self):
        return self.name + ' says woooooffffff!!'

class cat(Animal):

    def speak(self):
        return self.name + ' says meowww!!'

leo = dogg('Leo')
mani = cat('Mani')

print(leo.speak() + '\n' + mani.speak())



print('\nSpecial Methods')

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #to get object details, string representation for the object 
    def __str__(self):
        return f'{self.title} by {self.author}'

    #to get object length as normal len(obj) won't return correct length but just memory location
    def __len__(self):
        return self.pages

    #to get a message after object deletion
    ##def ___del__(self):
        ##print("Book object is deleted")

c = Book('Book1', 'Advait', 300)
#it won't be able to print it(like any list or tuple or set etc) as it will return the memory location where it is stored, so we have to use a special __str__ method
##print(b) ##o/p = <__main__.Book object at 0x000001EE0F889ED0>1

print(c)
print(len(c))
del c
#print(c)




        