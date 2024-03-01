### Python Lists ###

my_list = ["apple", "banana", "cherry"]

# Lists are used to store multiple items in a single vairable
# Lists are one of four built-in data types in Python used to store collections of data (Lists, Tuple, Set, Dictionary). These all have different qualities and usage. (SEE BELOW)

# Lists are created with Square Brackets [].

this_list = ["apple", "banana", "cherry"]
print(this_list)

# Lists items are ordered, changeable, and allow duplicate values.
# Ordered means that the items have a defined order, which will not change, new items added to a list will be placed at the end of the list.
# The list is changeable, we can change, add, and remove items from the list after it has been created.

# Lists are indexed, which allows to have items with the same value:
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

# To determine how many items a list has, use the len() function:
this_list = ["apple", "banana", "cherry"]
print(len(this_list))

# Lists can be any data type:

# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Or it can contain different data types:

# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

# Type()

# Python sees lists as objects with the data type 'list'

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # Prints  <class 'list'>

# The list() contructor can be used to make a new list:

this_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(this_list)

# Python Collections (Arrays)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

### Access List Items ###

# List items are indexed and can be accessed by referring to the index number
this_list = ["apple", "banana", "cherry"]
print(this_list[1])

# Negative Indexing - means start from the end - -1 refers to the last item, -2 refers to the second last item etc.
this_list = ["apple", "banana", "cherry"]
print(this_list[-1])

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range. - When specifying a range, the return value will be a new list with the specified terms.

# Return the third, fourth, and fifth item:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])

# This example returns the items from "cherry" to the end:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])

# Range of Negative Indexes

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])

# Check if Item Exists

# Check if "apple" is present in the list:

this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
  print("Yes, 'apple' is in the fruits list")

# Change List Items
  
# Change Item Value
  
# To change the value of a specific item, refer to the index number:
# Change the second item:

this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)

# Change a range of items

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Change the second value by replacing it with two new values:
this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Change the second and third value by replacing it with one value:
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)

# Insert Items

#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:

#Insert "watermelon" as the third item:
this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print(this_list)

# Add List Items

# Append Items

#To add an item to the end of the list, use the append() method:

#Using the append() method to append an item:
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)

# Insert Items

#To insert a list item at a specified index, use the insert() method.

#The insert() method inserts an item at the specified index:

#Insert an item as the second position:
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)

# Extend List

# Add the elements of tropical to thislist:

this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)

# Add Any Iterable

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Add elements of a tuple to a list:
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

# Remove List Items

# Remove Specified Item

# The remove() method removes the specified item.

# Remove "banana":
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)

# If there are more than one item with the specified value, the remove() method removes the first occurance:

# Remove the first occurance of "banana":
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove("banana")
print(this_list)

# Remove Specified Index

# The pop() method removed the specified index.

#Remove the second item:
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print(this_list)

# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index.

# Remove the first item:
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)

# The del keyword can also delete the list completely

#Delete the entire list:
this_list = ["apple", "banana", "cherry"]
del this_list

# Clear the List

# The clear() method empties the list.

# The list still remains, but it has no content.

# Clear the list content:
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)

# Loop Lists

# Loop Through a List

# You can loop through the list items by using a for loop:

#Print all items in the list, one by one:
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)

# Loop Through the Index Numbers
  
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Print all items by referring to their index number:
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
  print(this_list[i]) #Prints The iterable created in the example above is [0, 1, 2]

# Using a While Loop

#You can loop through the list items by using a while loop.
#Remember to increase the index by 1 after each iteration.

# Print all items, using a while loop to go through all the index numbers
this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
  print(this_list[i])
  i = i + 1

# Looping Using List Comprehension
  
# List Comprehension offers the shortest syntax for looping through lists:

# A short hand for loop that will print all items in a list:
this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]

# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]

print(new_list)