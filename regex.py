# search simple pattern 
import re

pattern = "a"
string = "abc"

if re.match(pattern, string):
    print("match found")
else:
    print("no match found")