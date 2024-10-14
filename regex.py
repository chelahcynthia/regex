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
    
# matching phone numbers 
text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\+?\d{1,3}[-.\s]\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?d{1,4}"
 
matches = re.findall(pattern,text)
print(matches)

# matching emails
text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
 
matches = re.findall(pattern,text)
print(matches)




    
 

