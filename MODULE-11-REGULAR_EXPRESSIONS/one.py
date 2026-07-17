import re
message="The current Python version is 3.13.  Othe previous version are 3.12 , 3.11 ,3.10"
#If python present in message
print("Python" in message)
print("13" in message)
print("11" in message)
print(message.find('3.13'))

match=re.search('13',message)
print(match)

if re.search('13',message):
    print("found")
else:
    print("Not found")

#syntax:: re.search(regex_pattern,string)