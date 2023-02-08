print('PYTHON DEBUGGER')

import pdb

x = 'a'
y = [1,2,3,4]
z = 3
a = 5

result1 = z + a
#set the trace
pdb.set_trace()
result2 = x + z  
result3 = x + y