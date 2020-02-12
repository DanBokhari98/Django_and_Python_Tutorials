#Functions
def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function {}".format(param1))

my_func()


def hello():
    return "hello"

str = hello()
print(str)

#Okay i get it

#Type checking to force input
def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, Integers only"

result = addNum(2,5)
print(result)

# LAMBDA
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))


#Now to do this using LAMBDA or anonomys Functions
lambda num: num%2 == 0

evens = filter(lambda num: num%2 == 0, mylist)
print(list(evens))



tweet = "Go sports! #Sports"
result = tweet.split('#')
print(result)
