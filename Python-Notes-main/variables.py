## Varibables ##
    
# There is no command for declaring a variable

x = 5
y = "Hello World!"
print(x)
print(y)

# Variables do not need to be declared with any particular type, they can be changed after they have been declared

x = 4  # This is a type of int
x = "Sally"  # This is a type of str
print(x)

# Casting (if you want to specify the type of a variable)

x = str(3)  # This will be '3'
y = int(3)  # This will be 3
z = float(3)  # This will be 3.0

# Getting the Type using the type() function

x = 5
y = 'John'
print(type(x))
print(type(y))

# Variable names are case sensitive

a = 4
A  = 'Sally'
#A will not overwrite a

# Legal variable names

myvar = 'John'
my_var = 'John'
myvar2 = "John"

# Illegal variable names

2myvar = "John"
my-var = "John"
my var = "John"

# Python generally uses snake case for declaring variables
declare_variable = x

# Camel case is okay too
declareVariable = x

# Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign One Value to multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking a collection of values in a list

fruits = ['apple', 'banana', 'cherry']
x, y , z = fruits
print(x)
print(y)
print(z)

# Printing multiple variables

x = 'Python '
y = 'is '
z = 'awesome'
print(x + y + z) # Note the extra space afer Python ans is so it prints correctly: Pythin is awesome. Without extra space: Pythonisawesome

# For numbers the + acts as a math operator
x = 5
y = 10
print(x + y)

# Only works with numbers

x = 5
y = 'John'
print(x + y) # This would error out

# Global Variables

x = 'awesome'

def my_func():
    print("Python is " + x)

my_func()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the fucntion. The global variable wih
# the same name will remain as it was, global and with the origial value

x = 'awesome'

def my_func():
    x = 'fantastic'
    print("Python is " + x)

my_func()

print("Python is " + x)

# The Global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, use the global keyword

def my_func():
    global x
    x = 'fantastic'

my_func()

print("Python is " + x)

# Also use the global keyword if you want to change a global variable inside a function

x = 'awesome'

def my_func():
    global x
    x = 'fantastic'

my_func()

print("Python is " + x)
