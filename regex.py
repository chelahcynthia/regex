# search simple pattern 
import re

pattern = "a"
string = "abc"

if re.match(pattern, string):
    print("match found")
else:
    print("no match found")
    

# Wildcard
pattern =r"a.b"
string ="acbb"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')
    

# character
pattern =r"[0-9]"
string ="0123"

if re.match(pattern,string):
    print('match founf')
else:
    print('no match found')