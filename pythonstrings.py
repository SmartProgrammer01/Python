# Python Strings


# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a+"\n")

# Get the character at position 1 (remember that the first character has the position 0):
  
a = "Hello, World!\n"
print(a[1]+"\n")


# Loop through the letters in the word "banana":

for x in "banana":
  print(x+"\n")


# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a),"\n")


# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)


# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)