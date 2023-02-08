print('MATH and RANDOM module')

print('\n Math Module')

import math

print('\n1. floor and ceil to round off a number')
num1 = 4.76
print(f'floor of {num1} = {math.floor(num1)} and ceil of {num1} = {math.ceil(num1)}')

print('\n2. mathematical constants')
print(f'pi = {math.pi}, e = {math.e}, infinity = {math.inf}, not a number = {math.nan}')

print('\n3. logarithms')
print(f'log to e base e = {math.log(math.e)} \nlog 100 to base 10 = {math.log(100,10)}')

print('\n Random module')

import random

print('\n1. Setting the seed')
# setting a seed helps to get the same sequence of random numbers. It is mainly useful when we are trying to test some functionality and want certain set of numbers as part of test cases
random.seed(20)
print('print fixed set of random integers')
print(random.randint(0, 200))
print(random.randint(0, 200))
print(random.randint(0, 200))
print(random.randint(0, 200))
print(random.randint(0, 200))
print(random.randint(0, 200))
print(random.randint(0, 200))

#tip - > comment the see line to get the expected results from here onwards 

print('\n2. Get a random number from the list of numbers from 0 to 30')
mylist = list(range(0,30))
print(random.choice(mylist))

print('\n2.1 get set of 10 numbers from list wwith replacement i.e. with repetation')
print(random.choices(population = mylist,k=10))
print('\n2.2 get set of 10 numbers from list wwithout replacement i.e. without repetation')
print(random.sample(population = mylist,k=10))

print('\n3. Shuffle the list, the shuffle happens in the list so the original list items will be different from their earlier position')
print(f'pre shuffle -> {mylist} \nand ')
{random.shuffle(mylist)}
print(f'\npost shuffle -> {mylist}')


print('\n4. Uniform distribution')
#it chooses a randome number(int or float (float with large precision)) from given start and values
print(f'\nbetween 10 and 11 -> {random.uniform(10,11)}')