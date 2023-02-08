print('REGULAR EXPRESSIONS')

import re

string = 'where is my phone, please ring my phone, my phone numer is - 3746723732'

pattern = 'phone'

#search() ->  find given pattern in given string, returns match object
#it will return the index location for that search as well, if multiple search result occur the only the first index location is shown
#if no match then nothing is returned, none 
#can be used as boolean values 
print(re.search(pattern, string))  #o/p = <re.Match object; span=(12, 17), match='phone'>
pattern2 = 'asfdasdf'
print(re.search(pattern2, string))

#findall returns all matching patterns
print(re.findall(pattern, string))

#finditer() -> returns an tuple of match objects which we can iter through
for m_obj in re.finditer(pattern, string):
    print(m_obj.span())
    print(f'{m_obj.start()} \t {m_obj.end()}')
    print(m_obj.group()) #matched pattern



string2 = 'where is my phone, please ring my phone, my phone numer is - +91 374-672-3732'

m = re.search(r"[+]+\d\d\s\d\d\d-\d\d\d-\d\d\d\d", string2)
print(m)
m = re.search(r"[+]\d{2}\s\d{3}-\d{3}-\d{4}", string2)
print(m)

#compile() -> compiles different regex patterns into one
#we can look for the specifix pattern in the result
#note - >  the indexing starts at 1 here and not 1

phone_pattern = re.compile(r"([+])(\d{2}) (\d{3})-(\d{3})-(\d{4})")
m2 = re.search(phone_pattern, string2)
i=1
while True:
    print(m2.group(i))
    i += 1
    if i > 4: 
        break
    


#| = or operator
s1 = 'there is a cat'
s2 = 'there is a dog'
for s in (s1,s2):
    print(re.search(r"cat|dog", s))

#. = wildcard operator
s3 = 'the cat sat on a rat wearing a hat'
print(re.findall(r".at", s3))  #note ->  based on number of characters before the actual pattern(here  -> 'at') we can adjust the numbers of dots

#^yourExpression  =  starts with and 
s3 = '1 is the number'
print(re.search(r'^\d', s3))

#yourExpression$  =  ends with 
s3 = 'the number is 1'
print(re.search(r'\d$', s3))

#[^yourExpression] = to exclude certain things from given text
#[] - > basically the square bracket are used to group the things together  - aka - inclusion
#very useful for removing the puctuations from the string to process it better
s3 = 'this is a string! need to remove punctuations from it. could you help please?'
print(f'phrase = {s3}')
pattern = r'[^!.?]'
s3_1 = re.findall(pattern, s3)
print(f'new phrase = {s3_1}')   #shows all individual letters
#to get all words , notice added spacce here in pattern afer '?' symbol
pattern = r'[^!.? ]+'
s3_2 = re.findall(pattern, s3)
print(f'updated phrase -> {s3_2}')

#get the string back again
print(f'clean string -> {" ".join(s3_2)}')


#find hypenated words
s3 = 'find hypen-ated words in this sentence, hopefully that wont take too-much time'
pattern = r'[\w]+-[\w]+'  #also equal to = r'\w+-\w+'
print(re.findall(pattern, s3))

#() ->  uised for checking multiple options of matching
#find words that start with cat
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

pattern = r'cat(fish|nap|erpillar)'

for s in (text,texttwo,textthree):
    print(re.search(pattern, s))
