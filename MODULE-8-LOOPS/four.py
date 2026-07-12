import random
print(random.random())
print(random.randint(10,15))
nums=[10,4,1,8,4,3]
print(random.choice(nums))

fruits=["Apple","Orange","Mango"]
random.shuffle(fruits)
print(fruits)