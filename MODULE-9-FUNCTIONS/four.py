add =lambda x:x+10
print(add(15))

multiply=lambda y:y*10
print(multiply(12))

seq=[1,2,3,4]
add=lambda x:True if x%2!=0 else False
filtered=filter(add,seq)
print(list(filtered))

add1=lambda x:True if x%2!=0 else False
mapped=map(add1,seq)
print(list(mapped))