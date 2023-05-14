import  test1 
print (test1.test(2,3))
print ("Hello this is taken from test1 module",test1.test(2,3))
print (test1.test(1,2))

from test1 import testa 
print (testa(2,3))
# print (testa())

print (dir())



