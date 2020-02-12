s = "django"

print(s[0])
print(s[5])
print(s[0:4])
print(s[1:4])
print(s[4:6])
print()
print(s[::-1])


#problem 2

l = [3,4,[1,4,'hello']]

l[2][2] = "goodbye";
print(l)


#problem 3

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}


#Solution
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
print();


#problem 4

mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3]
print(set(mylist))


#problem 5
age = 4
name = "Sammy"

print("Hello my dog's name is {a} and he is {b} age years old".format(a=name, b=age))
