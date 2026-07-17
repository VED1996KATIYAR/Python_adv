import re
message="The current aa ab abbba ddk aab aabbb aaaabbbb version of python is 3.13 . Other prvious version are 3.12,3.11,3.10"
pat=r"[a-z]*"
print(re.search(pat,message))
pat=r"[a-z]+"
print(re.search(pat,message))
pat=r"[a-z]?"
print(re.search(pat,message))
pat=r"a{3}"
print(re.search(pat,message))

pat=r"a{3,}"
print(re.search(pat,message))