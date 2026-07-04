numbers=[0,1,3,4,1,0,5,0,0,3,0]
print(f"The list is: {numbers}")
items=int(input("Enter the number to count: "))
count=numbers.count(items)
print(f"The number {items} appears {count} times in the list.")


language=["Python","Java","C++","JavaScript","C#"]
print("Python" in language)  # Output: True
print("Ruby" in language)    # Output: False

print("Python" not in language)  # Output: False
print("Ruby" not in language)    # Output: True