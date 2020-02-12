t1 = [1,1,2,3,1]
t2 = [1,1,2,4,1]
t3 = [1,1,2,1,2,3]
seq = [1,2,3]

def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    else:
        return False


print(arrayCheck(t1))
print(arrayCheck(t2))
print(arrayCheck(t3))

def stringBits(str):
    ans = ""
    for i in range(len(str)):
        if i % 2 == 0:
            ans = ans + str[i]
    return ans

result = stringBits("Hello")
print(result)




def end_other(a,b):
    a = a.lower()
    b = b.lower()
    #return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]

print(end_other('Hiabc', 'abc'))
print(end_other('Abc', 'Hiabc'))
print(end_other('abc', 'abxabc'))


def doubleChar(str):
    ans = ""
    for i in range(len(str)):
        ans = ans + str[i] + str[i]
    return ans

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n

res = no_teen_sum(2,1,14)
print(res)
