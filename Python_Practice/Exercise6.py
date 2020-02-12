mypair = [(1,2), (3,4), (5,6)]


#Tuple unpacking
for tup1, tup2 in mypair:
    print(tup1)
    print(tup2)


#Dont normally do this but okay.


#While loops

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i + 1;

x = [1,2,3,4]
#List comprehension
out = [i**2 for i in x]


print(out)
