# # # --------------------------ALL About Functions ------------------------ # #  #

#Declaring a Function


def brush_teeth(): #brush_teeth is the function name, def is used to define a function
    print("take the toothbrush") #these three print lines are function body // sub tasks
    print("Clean teeth with it")
    print("Rinse your mouth")

print("Now call the function")
brush_teeth() #call function name to execute, to call/execute a function -- function_name()  -- open and close paranthesis after the name is mandatory

#Using parameter or argument in function
# Variable declared as a parameter is only available inside that function only
def five_times(num):
    print(num*5)

five_times(7)
x = 9
five_times(9)





#Using return
def mul_numbers(num1, num2):
    return (num1 * num2) # You can return any type of data type

mult = mul_numbers(11, 5)
print(mult)





#A function example

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact
print(factorial(5))





#Recursive Function
# TO call the function inside of the function is called a recursive function
def factorialRecursive(num):
    if num <= 1:
        return 1
    else:
        return num * factorialRecursive(num - 1)

print(factorialRecursive(7))






#Using default value as a parameter Funtion
def defaultValueFunction(val1, val2=5):         #Non-default values follow default argument
    return val1 * val2

print(defaultValueFunction(6, 6))
print(defaultValueFunction(6))





#Argument/Parameter Order not to be maintained if you pass it by their name
def simplesub(a, b):
    return a - b

print(simplesub(10, 5))
print(simplesub(b = 5, a = 10)) #both print will give same result




#Anonymous or Lambda Function - One line function
double = lambda x: x * 2
print(double(5))






#Using global variable inside a function -- Study more about it
c = 6
def add(a, b):
    c = a + b  # this c variable is different from the global c variable
    return c
print(add(3, 6))
print(c)




c = 7   #Global variables are the variables that are not within any scope(any block of code), and are declared at the beginning of the program
d = 8
def add1(a, b):
    print(d)    #You can read a global variable inside a function, but can't write it unless you call it using the kw -- global --
    global c # that's how to call a global variable inside a function to modify its value
    c = a + b # this c is the global variable, its value has been changed
    return c
print(add1(10, 5))
print(c)





#Queries
# What about variable declared in a function ( not as a parameter/argument), can we call it from outside of the function?
# When and what happens when we use function parameter as (*args) - may be in those cases when we don't know how many parameters a user might pass

#Important Notes:
# #You can call a function from another Function 
# Variable declared as a parameter is only available inside that function only
# Return KW can return any data types as well as lists, tuple, dictionary, class or a dataclass
# Recursive Function calls itself
# You can set a default value to a parameter ( def functionName (value = 5) this default value will be used if you do not pass any parameter through it)
# Your don't have to worry about parameter order, if you pass it by their name while calling functions
# All built in funtions of python: docs.python.org/3/library/functions.html
# Do not forget to use ANonymous function / Lambda function, where necessary