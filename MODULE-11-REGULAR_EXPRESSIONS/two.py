import re
message="The current version of Python is 3.13 . the older version is 3.12,3.11,3.10"
match=re.search("[0-9][0-9]",message)
print(match)
match1=re.search("[0-9][0-9][0-9]",message)
print(match1)
match3=re.search("[0-9][.][0-9][0-9]",message)
print(match3)
match4=re.search("[0-9].[0-9][0-9]",message)