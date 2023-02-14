print('ADVANCED')
#python has built in math library which has different mathematical functions. Other than that here are couple of functions directly available without importing math available

print('\n1. Numbers')

#hex() -
print(f'\n12 in hexdecimal is = {hex(12)}')
#bin() -
print(f'12 in binary is = {bin(12)}')
#pow() -
print(f'3 to the power 5 is = {pow(3,5)}')  #there is another third argument which is used to take mod
#round() - ot always returns a float
print(f'3.141592 round off to 2 digits isis = {round(3.14,2)}')
#abs() -
print(f'absolute of -3 is = {abs(-3)}')


print('\n1. Strings')

string = 'hello world'

print(f'\ncapitalize first letter -> {string.capitalize()}')
print(f'make all letters upper case -> {string.upper()}')
print(f'make all letters lower case -> {string.lower()}')
print(f'count number of o -> {string.count("o")}')
print(f'find o -> {string.find("o")}')   #returns first index
print(f'center the string between 30 z -> {string.center(30,"z")}')
s = 'hi\tthere'
print(f'expand tabs for given string -> {s.expandtabs()}')
print(f'check if all letteres are alphanumberic -> {string.isalnum()}')
print(f'check if all letteres are alphabets -> {string.isalpha()}')
print(f'check if all chars are lowercase -> {string.islower()}')
print(f'check if all chars are uppercase -> {string.isupper()}')
print(f'check if this is a whitespace string -> {string.isspace()}')
print(f'check if this is a title string -> {string.istitle()}')
print(f'check if the string ends with d -> {string.endswith("d")}')   #its equal to string[-1]=='d'
print(f'split the string at o -> {string.split("o")}')
print(f'partition the string at first instance of l -> {string.partition("l")}')   #it returns first half(head), the separator, other hald(tail)




print('\n1. Sets ')

s = set()
for i in range(1,6):
    s.add(i)
print(f'Add number 1 to 5 to set s {s}')
s.clear()
print(f'empty the set -> {s}')
s = {1,2,5}
s_copy = s.copy()
print(f'copy set s to another set -> s = {s}, s_copy = {s_copy}')   #changes in s does not affect s_copy
s.add(3)
s.add(9)
print(f'difference between s and s_copy -> {s.difference(s_copy)}')
print(f's = {s}  s_copy = {s_copy}')
s.difference_update(s_copy)
print(f'update s with difference between s and s_copy-> {s}')
{s.discard(9)}
print(f'discard 9 from s -> s = {s}')   #does not return any error if element is not available in the set
s1 = {1,4,6,7,8}
s2 = {8,7,6,3}
print(f's1 = {s1}')
print(f's2 = {s2}')
print(f'Intersection of s1 and s2 -> {s1.intersection(s2)}')
print(f'update s1 with Intersection of s1 and s2 -> s1 = {s1.intersection(s2)}')

s1 = {1,6}
s2 = {1,6,3}
s3 = {5}

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's3 = {s3}')
print(f'chek if s1 and s2 are joint -> {s1.isdisjoint(s2)}')    #returns true if given sets have no intersection 
print(f'chek if s1 and s3 are joint -> {s1.isdisjoint(s3)}')
print(f'chek if s3 and s2 are joint -> {s3.isdisjoint(s2)}')
print(f'check if s1 is subset of s2 -> {s1.issubset(s2)}')
print(f'check if s2 is superset of s1 -> {s2.issuperset(s1)}')
print(f'Symmetric difference of s1 and s2 -> {s1.symmetric_difference(s2)}')      #opposite of intersection, return all elements that are exactly in one set, in this case its 3
{s1.symmetric_difference_update(s2)}
print(f'update s1 with Symmetric difference of s1 and s2 -> s1 = {s1}')      #updates s1 with symmetric differenc between s1 and s2
print(f'get union of s1 s2 and s3 -> {s2.union(s3)}')
{s3.update(s2)}
print(f'update s3 with s1 -> s3 = {s3}')



print('\nDictionaries')

d = {'k1':1,'k2':2}
print('Dictionary Comprehension')
print('create a dictionary using Dict. Compre. with square of numbers from 1 to 10')
print({x:pow(x,2) for x in range(1,11)})
print('assign keys as  fisrt 10 aplhabets to above dictionary')
alphabets_10 = ['a','b','c','d','e','f','g','h','i','j']
print({k:pow(v,2) for k,v in zip(alphabets_10,range(1,11))})
print(f'iterate over keys in {d}')
for k in d.keys():
    print(k)
print('iterate over values')
for k in d.values():
    print(k)
#use viewitem, viewkeys, viewvalues for python2



print('\nLists')

l = [1,3,3]
print(l)
l.append(5)
print(f'append 5 to list  ->  {l}')
print(f'count of 3   ->   {l.count(3)}')
l.extend([7,6,4])    #extend will add each element of given list to original list whereas apend willl given list as an element to original list
print(f'extend the list with [7,6,4]   ->   {l}')
print(f'find index of 4  ->  {l.index(4)}')    #returns error if element is not available
l.insert(2, 'inserted')
print(f'insert "inserted" at index 2   ->   {l}')
print(f'pop 3rd element  ->  {l.pop(3)}')     #default index is -1
l.insert(3,3)
l.remove(3)
print(f'remove first instance of 3    ->  {l}')
{l.reverse()}
print(f'reverse the list   ->   {l}')
l.remove('inserted')
{l.sort()}
print(f'sort the list   ->  {l}')
