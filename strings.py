# Strings Methods:

## String Slice:

# String slicing in Python allows you to access a substring of a string by specifying a range of indices. The syntax for string slicing is:
# string[start:stop:step]
# start is the index where the slice begins (inclusive).
# stop is the index where the slice ends (exclusive).
# step is the interval between each character in the slice (optional).


s = "Hello World"

# Slice from index 0 to 5 (excluding 5)
slice1 = s[0:5]
print(slice1) # Hello


# Slice from index 7 to the end
slice2 = s[7:]
print(slice2) # orld

# Slice from the beginning to index 5 (excluding 5)
slice3 = s[:5]
print(slice3) # Hello

# Slice the entire string
slice4 = s[:]
print(slice4) # Hello World



## Slicing with Skip Value

# Slice with a step of 2
slice5 = s[::2]
print(slice5)  # Hlowrd

# Slice from index 1 to 8 with a step of 2
slice6 = s[1:8:2]
print(slice6)  # el w0

# Negative indices: slice from index -6 to the end
slice7 = s[-6:]
print(slice7) # World

# Negative step: reverse the string
slice8 = s[::-1]
print(slice8) # dlroW olleH

## String Function

# capitalize() : Capitalizes the first character of the string.
string = "hello world"
print(string.capitalize()) # Hello world

# casefold(): Converts the string to lowercase in a way that is suitable for caseless comparisons.
string1 = "HELLO WORLD"    
print(string.casefold()) # hello world

# endswith(): Returns True if the string ends with the given number.
string2 = 'AbdulRehman'
print(string2.endswith("man")) # True

# center(width[, fillchar]): Centers the string in a field of specified width.
string3 = "Hello"
print(string3.center(10 , "-")) # --Hello---

# count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of a substring.
string4 = "Hello World"
print(string4.count("l")) # 3
print(string4.count("o")) # 2 

# find(sub[, start[, end]]): Returns the lowest index of the substring.
string5 = "Hello World"
print(string5.find('W')) # 6
print(string5.find('l')) # 2

# index(sub[, start[, end]]): Returns the lowest index of the substring, raises ValueError if not found.
string6 = "Hello World"
print(string.index("o")) # 4

# isalnum(): Checks if all characters are alphanumeric.
string7 = "hello123"
print(string7.isalnum()) # True

#isalpha(): Checks if all characters are alphabetic.
string8 = "hello"
print(string8.isalpha()) # True

# expandtabs([tabsize]): Replaces tabs with spaces.
string9 = "hello\tworld"
print(string9.expandtabs(10)) # hello     world

# join(iterable): Joins elements of an iterable with the string as a separator.
string11 = "-"
print(string11.join(["a","b","c","d"])) # a-b-c-d

# replace(old, new[, count]): Replaces occurrences of a substring.
string12 = 'Hello World'
print(string12.replace("World", "Python")) # Hello Python

# split(sep=None, maxsplit=-1): Splits the string.
string13 = "a b c d e"
print(string13.split()) # ['a', 'b', 'c', 'd', 'e']

# The len() function in Python is used to determine the length (number of items) of an object.
s = "Hello, World!"
print(len(s))  # Output: 13

lst = [1, 2, 3, 4, 5]
print(len(lst))  # Output: 5

tup = (1, 2, 3)
print(len(tup))  # Output: 3