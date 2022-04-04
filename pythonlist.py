# Python Lists


# Lists are created using square brackets:


thislist = ["apple", "banana", "cherry"]
print(thislist) # prints the list


# Since lists are indexed, lists can have items with the same value:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # Prints the list


# To determine how many items a list has, use the len() function:


thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Prints the length of the list


# To retrieve a list item, use the index number:


thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Prints the second item in the list


# To change the value of a list item, use the index number to identify the item:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # Changes the second item in the list


# To determine if a specified item is in a list, you can use the in keyword:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list") 


# To loop through all the items in a list, use a for loop:


thislist = ["apple", "banana", "cherry"]
for x in thislist: 
    print(x) # Prints the list items


# To determine the index of an item in a list, use the .index() method:


thislist = ["apple", "banana", "cherry"]
print(thislist.index("banana")) # Prints the index of the item


# To add an item to the end of the list, use the append() method:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # Adds an item to the end of the list


# To add an item at the specified index, use the insert() method:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # Inserts "orange" at index 1
print(thislist) # Prints the list


# The remove() method removes the specified item:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # Removes the first item with the value "banana"
print(thislist) # Prints the list


# The pop() method removes the specified index, (or the last item if index is not specified):


thislist = ["apple", "banana", "cherry"]
thislist.pop() # Removes the last item in the list
print(thislist) # Prints the list


# The del keyword removes the specified index:


thislist = ["apple", "banana", "cherry"]
del thislist[0] # Removes the first item in the list
print(thislist) # Prints the list


# The clear() method empties the list:


thislist = ["apple", "banana", "cherry"]
thislist.clear() # Removes all items from the list
print(thislist) # Prints the list


# The list() Constructor creates a list:


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # Prints the list


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()      
print(thislist)  


# The reverse() method reverses the order of the items in the list:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist)


# The min() and max() methods return the minimum and maximum values in the list:


thislist = ["apple", "banana", "cherry"]
print(min(thislist)) # Prints the minimum value in the list
print(max(thislist)) # Prints the maximum value in the list


# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)




