print('COLLECTIONS')
#collections module has many sub modules which are mostly a specialized version of python datatypes.
print('\n1. Counter Class')
#import the counter module

from collections import Counter
print('1.1 Count each unique item in the given list')
mylist = [1,1,3,2,1,2,3,3,2,4,4,4,5,4,2,5,3,2,5,5,4,3]
print(Counter(mylist))
mylist2 = ['b','b','b',10,10,3,2,2,0.5]
print(Counter(mylist2))
str = 'asihdbdfsdbsxjzxkjsjkakjdnasldASJD'
print(Counter(str))
x = Counter(str)
print(f'most common letter in this strings {str},\n{x.most_common()}')
sentence = 'the number of times a word comes up in a this sentence'
print(Counter(sentence.split()))

print('\n2. Default Dictionary')

from collections import defaultdict
#it assignes a defaukt value when a key error happens i.e  key is unavailable

d =  defaultdict(lambda: 200)
d['n'] = 300
print(f"c = {d['c']}, d = {d}")

print('\n2. Named Tuple')
#expand on normal tuple object by giving named indices in case of very large tuple or we forgot which value is at which position
from collections import namedtuple

Dog =  namedtuple('Dog', ['Age','Breed','Name'])

sammy = Dog(Age = 6, Breed='Chihuahua',Name='Sammy')

print(type(sammy))
print(sammy)

print(f'{sammy.Age}, {sammy.Breed},{sammy.Name}')

