import math
# String data type

# literal assignment
strs = "Hey Shivam!"
print(type(strs) == str)
print(isinstance(strs, str))

newStr = str("new");
print(type(newStr) == str)
print(newStr)

# Concatination

str1 = "Hello"
str2 = "World"
str1 = str1 + " " + str2
str1 += "!"
print(str1)

# casting conversions
decade = str(1980)
print(decade)
print(type(decade))

# multilines
multiline = '''
  This is a multiline xyz abc
        example!!
'''

print(multiline)

# escaping special characters
sentence = 'shivam\'s notebook\t is new'
print(sentence)

# string methods
first ='abc'
second = 'xyz'

print(first.lower() + second.upper())
print(multiline.title())
print(multiline.replace(first, second))
print(len(multiline))

# build a menu
title = "menu".upper()
print(title.center(20, "-"))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$2".rjust(4))
print("BananaCake".ljust(16, '.') + "$5".rjust(4))

# string index values
print(first[0])
print(first[-1])
print(first[0:2])
print(first[0:])

# methods returns boolean
print(first.startswith('a'))

# integer
someInt = int(20)
print(someInt)

# float

someFloat = float(20)
print(someFloat)

# complex numbers

someComplex = complex(20 + 30j)
print(type(someComplex))
print(someComplex.real)
print(someComplex.imag)

print(math.pi)
