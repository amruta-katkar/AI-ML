str = "data science lecture 3 string operatins"
print(str)

para = ''' this is long 
paragraph'''

print(para)

print(type(str))
print(type(para))

print(str[7])
print(str[:8])
print(str[7:10])
str2 = " ".join(reversed(str))
print(str2)

str3 = "{} {} {}".format("hello", "world", "python")
print(str3)

# string functions

str = "data science AI ML lecture 3"
print(str.capitalize()) # first letter capital and rest small
print(str.casefold()) # all small
print(str.center(50,"*")) # center the string with * in between
print(str.count("a")) # count the number of a in the string
print(str.lower())
print(str.upper())
print(str.endswith("3"))
print(str.startswith("data"))
print(str.find("AI"))
str2 = " kwhd"
print(str2.isalnum()) # check if all characters are alphanumeric
str3 = "345678xcvbn"
print(str3.isalpha()) # check if all characters are alphabets

str4 = "5678"
print(str4.isdigit()) # check if all characters are digeit

str2 = "Hello"
print(str2.istitle())
