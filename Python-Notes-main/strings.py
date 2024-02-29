# Strings

# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays

# Get the character at position 1 (remember that the first character has the position 0)

a = 'hello world'
print(a[1])

# Since strings are arrays, we can loop through the characters in a string with the for loop

for x in 'banana':
    print(x)

# String Length

# To get the length of a string use the len() function.
    
a = 'hello world'
print(len(a))

# Check String

# To check and see if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

# use it in an if statement

txt = "The best things in life are free!"
if 'free' in txt:
    print("Yes, 'free' is present")

# To check and see if a certain phrase or character in NOT present in a string, we can use the keyword not in.
    
txt = "The best things in life are free!"
print("expensive" not in txt)

# use it in an if statement

txt = "The best things in life are free!"
if 'expensive' not in txt:
    print("No, 'expensive' is NOT present")

### SLICING STRINGS ###
    
# You can return a range of characters by using the slice syntax.

b = 'Hello World!'
print(b[2:5]) # Prints 'llo '

# Slicing from the start.
b = 'Hello World!'
print(b[:5]) # Prints 'Hello '

# Slicing from the end.
b = 'Hello World!'
print(b[2:]) # Prints 'llo World!'

# Negative Indexing

# Get the characters: From 'o' in "World!" (postition -5) to, but not included: 'd' in "World!" (position -2)
b = 'Hello World!'
print(b[-5:-2]) 

### MODIFY STRINGS ###

# Change string to UPPER CASE

a = 'Hello World!'
print(a.upper())

# Change string to lower case

print(a.lower())
 
# Remove Whitespace

# Whitespace is the space before and/or after actual text, and quite often we want to remove this space

a = " Hello World! "
print(a.strip()) # Prints "Hello World!"

# Replace String

a = "Hello World!"
print(a.replace("H", "J")) # Prints "Jello World!"

# Split String

# The split() method returns a list where the text between the speicifed separator becomes the list items

a = "Hello, World!"
print(a.split(",")) # Prints ["Hello" , "World!"]

# Concatenation

# To concatenate, or combine, two strings you can use the + operator

a = 'Hello'
b = 'World!'
c = a + b
print(c)

# To add a space between them, add a " "

a = 'Hello'
b = 'World!'
c = a + " " + b
print(c)

# String Format

# WE CANNOT DO THIS, IT WILL THROW AN ERROR

#age = 36
#txt = "My name is John, I am" + age
#print(txt)

# To combine strings and numbers we can use the format() method

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 3
item_num = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_num, price))

# You can use index numbers to be sure the arguments are placed in the correct placeholders.

quantity = 3
item_num = 567
price = 49.95
my_order = "I want {2} pieces of item {0} for {1} dollars."
print(my_order.format(quantity, item_num, price))

## String Methods:
  #Method	           Description
capitalize()	#Converts the first character to upper case
casefold()	    #Converts string into lower case
center()	    #Returns a centered string
count()	        #Returns the number of times a specified value occurs in a string
encode()	    #Returns an encoded version of the string
endswith()	    #Returns true if the string ends with the specified value
expandtabs()	#Sets the tab size of the string
find()	        #Searches the string for a specified value and returns the position of where it was found
format()	    #Formats specified values in a string
format_map()	#Formats specified values in a string
index()	        #Searches the string for a specified value and returns the position of where it was found
isascii()	    #Returns True if all characters in the string are ascii characters
isalnum()	    #Returns True if all characters in the string are alphanumeric
isdecimal()	    #Returns True if all characters in the string are decimals
isdigit()	    #Returns True if all characters in the string are digits
isidentifier()	#Returns True if the string is an identifier
islower()	    #Returns True if all characters in the string are lower case
isalpha()	    #Returns True if all characters in the string are in the alphabet
isnumeric()	    #Returns True if all characters in the string are numeric
isprintable()	#Returns True if all characters in the string are printable
isspace()	    #Returns True if all characters in the string are whitespaces
istitle()	    #Returns True if the string follows the rules of a title
isupper()	    #Returns True if all characters in the string are upper case
join()	        #Joins the elements of an iterable to the end of the string
ljust()	        #Returns a left justified version of the string
lower()	        #Converts a string into lower case
lstrip()	    #Returns a left trim version of the string
maketrans()	    #Returns a translation table to be used in translations
partition()    	#Returns a tuple where the string is parted into three parts
replace()	    #Returns a string where a specified value is replaced with a specified value
rfind()	        #Searches the string for a specified value and returns the last position of where it was found
rindex()	    #Searches the string for a specified value and returns the last position of where it was found
rjust()	        #Returns a right justified version of the string
rpartition()	#Returns a tuple where the string is parted into three parts
rsplit()	    #Splits the string at the specified separator, and returns a list
rstrip()	    #Returns a right trim version of the string
split()	        #Splits the string at the specified separator, and returns a list
splitlines()	#Splits the string at line breaks and returns a list
startswith()	#Returns true if the string starts with the specified value
strip()         #Returns a trimmed version of the string
swapcase()	    #Swaps cases, lower case becomes upper case and vice versa
title()	        #Converts the first character of each word to upper case
translate()   	#Returns a translated string
upper()	        #Converts a string into upper case
zfill()	        #Fills the string with a specified number of 0 values at the beginning