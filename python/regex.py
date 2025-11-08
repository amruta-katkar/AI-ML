# lecture5 --> Regex
# create regex
import re
str = "this is sentence"
# search for pattern
match = re.search(r'\b\w+\b', str)
# print match
print(match.end())



# email regex
import re
str = "example@gmail.com"
# search for pattern
match = re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z]',str)
# print match
print(match)


result = re.compile('\b')
print(result.findall("18 may 2024"))

result = re.compile('ab*')
print(result.findall("abbabbbaaaa"))

def validate_mail(mail):
    regex_email = '[A-Za-Z0-9]+@[a-zA-z0-9]+.[a-zA-z{1-3}]$'
    if re.match(regex_email, mail):
        return True
    else:
        return False
mail = "example@gmail.com"
print(validate_mail(mail))


