# Python tuples


# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# You can access tuple items by referring to the index number, inside square brackets:


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# You can loop through the tuple items by using a for loop:


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# You can check if a specified item is present in the tuple by using the in keyword:


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple") # Yes, 'apple' is in the fruits tuple


# You can specify a tuple with different data types:


thistuple = ("apple", "banana", "cherry", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(thistuple)


# You can use the tuple() constructor to make a tuple:


thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# You can convert a tuple into a string by using the str() function:


thistuple = ("apple", "banana", "cherry")
print(str(thistuple))


# You can get the length of a tuple by using the len() method:


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# You can delete a tuple completely by using the del keyword:


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # this will raise an error because the tuple no longer exists


# You can use tuples as function arguments and return a tuple:


def multiply(x, y):
    return x * y    # this function multiplies two numbers and returns the result


print(multiply(2, 3)) # this will print 6


# YouNegative indexing means start from the end.

#-1 refers to the last item, -2 refers to the second last item etc.


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])




# Tuples are immutable, which means you cannot change the value of a tuple once it is created.


thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # this will raise an error because tuples are immutable
print(thistuple)


# Tuples can be concatenated with the + operator:


thistuple = ("apple", "banana", "cherry")
thistuple2 = ("blackcurrant", "orange", "blueberry")
thistuple3 = thistuple + thistuple2
print(thistuple3)


# Tuples can be repeated with * operator:


thistuple = ("apple", "banana", "cherry")
thistuple4 = thistuple * 2
print(thistuple4)


# Tuples are hashable which means they can be used as keys in a dictionary:


thistuple = ("apple", "banana", "cherry")
mylist = ["apple", "banana", "cherry"]
mydict = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(mydict[thistuple[1]])


# Tuples can be used as a key in a dictionary:


thistuple = ("apple", "banana", "cherry")
mydict = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(mydict[thistuple])


# You can specify a range of indexes by specifying where to start and where to end the range.


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])












