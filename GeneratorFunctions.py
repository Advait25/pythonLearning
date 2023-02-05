print('GENERATOR FUNCTIONS')

print('\nExample 1. Cube of number from 1 o 10')

n = range(1,11)
def get_cube(n):

    for i in n:
        yield i**3          #yield keyword helps in generating the values as needed

print(get_cube(n))  # output -> <generator object get_cube at 0x7fccb9df25e0>

#now just like range function we can iterate through get cube function

#for i in get_cube(n):
#    print(i)

# we can cast it into a list if needed

print(list(get_cube(n)))


print('\nExample 2. Fibonacci Series')

def gen_fibonacci(n):
    a = 0
    b = 1

    for i in n:
        yield a
        a,b = b,a+b  # tuple unpacking to getting new number and store it

#for i in gen_fibonacci(n):
#    print(i)

print(list(gen_fibonacci(n)))



print('\nExample 3. next and iter function')

x = gen_fibonacci(n)
#next function 
print(next(x))
print(next(x))
print(next(x))

#iter function  
str = 'python learning'
string_chars = iter(str)
print(next(string_chars))
print(next(string_chars))
print(next(string_chars))

