#
# Example file for working with functions
#

# define a basic function
def func1():
    print("Function 1")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

# function that returns a value
def func3(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result


#function with variable number of arguments, where *args will take multiple 
#arguments in a function

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#func1()
#print(func1())
#print(func1)

func2(10,20)
print(func2(5,10))
print(func3(5))

print(power(2))
print(power(3,5))
print(power(x=5, num=3))
#both the lines 36 and 37 will return the same

print(multi_add(3,4,5,6,7))