#Decorators
print('PYTHON DECORATORS')

#some func
def func():
    print('hello')

print('1.assigning functions ')

greet = func

greet()

#even if the original func is deleted, new varibale will keep the function

print('deleting func')

del func

greet()

print('Example 1....greet inside hello')
def hello(name):

    print(f'hello {name}')

    def greet(name):
        print(f'greetings {name} greet() func inside hello() function')

    return greet


new_func = hello('Advait')
new_func('Advait')

print('Example 2....passing function x as an argument to y')

def x():
    return 'hello from x'

def y(some_func):
    print('Y func...now executing x from argument')
    print(some_func())

y(x)



print('\nCreating decoretor from above idea')
print('\n 1.with func inside func')

def decorator_func(original_func):

    def wrapper():

        print('decorating the func with wrap paper....')

        original_func()

        print('still decoarating..........\tand done!!!')

    return wrapper


def a ():
    print('a needs some wrapping..')

after_decoration = decorator_func(a)

after_decoration()

print('\n 2.with decorator syntax i.e.using @')

@decorator_func
def a():
    print('a needs some wrapping..')

a()