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

