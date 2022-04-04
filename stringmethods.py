# String methods    

#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper()) # returns "HELLO, WORLD!"


# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower()) # returns "hello, world!"


# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# The replace() method replaces a string with another string:

a = "Hat is the best thing ever!"
print(a.replace("H", "C")) # returns "Cat is the best thing ever!"



# The split() method splits the string into substrings if it finds instances of the separator:

a = "Pranav Kokate"
print(a.split(" ")) # returns ['Pranav', ' Kokate']


# The capitalize() method returns a string with the first character capitalized:

a = "this is string"
print(a.capitalize()) # returns "This is string"


# The title() method returns a string with each word capitalized:

a = "this is title"
print(a.title()) # returns "This Is Title"


# The isalpha() method returns True if all characters in the string are alphabetic and there is at least one character, False otherwise:

a = "Python"
print(a.isalpha()) # returns True


# The isdigit() method returns True if all characters in the string are digits and there is at least one character, False otherwise:

a = "12345"
print(a.isdigit()) # returns True


# The isalnum() method returns True if all characters in the string are alphanumeric and there is at least one character, False otherwise:

a = "Python3"
print(a.isalnum()) # returns True


# The islower() method returns True if all characters in the string are lowercase and there is at least one character, False otherwise:

a = "Python"
print(a.islower()) # returns False


# The isupper() method returns True if all characters in the string are uppercase and there is at least one character, False otherwise:

a = "PYTHON"
print(a.isupper()) # returns True


# The isspace() method returns True if all characters in the string are whitespace characters and there is at least one character, False otherwise:

a = " "
print(a.isspace())  # returns True


# The startswith() method returns True if the string starts with the characters in the specified string, False otherwise:

a = "Python"
print(a.startswith("Py")) # returns True


# The endswith() method returns True if the string ends with the characters in the specified string, False otherwise:

a = "Python"
print(a.endswith("on")) # returns True


# The istitle() method returns True if the string follows the rules of a title, False otherwise:

a = "It Is Title"
print(a.istitle()) # returns True


# The isdecimal() method returns True if the string contains only decimal characters and there is at least one character, False otherwise:

a = "12345"
print(a.isdecimal()) # returns True


# The isidentifier() method returns True if the string is an identifier and there is at least one character, False otherwise:

a = "Python3"
print(a.isidentifier()) # returns True


# The isprintable() method returns True if the string is printable and there is at least one character, False otherwise:

a = "Python"
print(a.isprintable()) # returns True


# The join() method joins the elements of an iterable to the end of the string:

a = "Python"
print(a.join(["-", "="])) # returns "-Python-"


# The ljust() method returns a left-justified version of the string:


a = "Python"
print(a.ljust(20)) # returns "Python               "


# The rjust() method returns a right-justified version of the string:


a = "Python"
print(a.rjust(20)) # returns "               Python"


# The center() method returns a centered version of the string:


a = "Python"
print(a.center(20)) # returns "      Python      "


# The zfill() method returns the numeric string left-filled with zeros:


a = "123"
print(a.zfill(5)) # returns "00123"


# The expandtabs() method returns the string where all tab characters are expanded using the tabsize argument:


a = "Python\tProgramming"
print(a.expandtabs(20)) # returns "Python               Programming"


# The count() method returns the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation:


a = "Python Programming"
print(a.count("o")) # returns 4


# The find() method returns the lowest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Returns -1 if sub is not found:


a = "Python Programming"
print(a.find("o")) # returns 4


# The rfind() method returns the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Returns -1 if sub is not found:


a = "Python Programming"
print(a.rfind("o")) # returns 9


# The index() method is similar to find(), but raises a ValueError when the substring is not found:


a = "Python Programming"
print(a.index("o")) # returns 4


# The rindex() method is similar to rfind(), but raises a ValueError when the substring is not found:


a = "Python Programming"
print(a.rindex("o")) # returns 9



























