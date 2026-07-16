file_handler=open("file3.txt",'rt')

# file_handler.write("Hello How are you \n")
# file_handler.write("Have A nice day \n")
# file_handler.write("Have a deep sleep")

# content=file_handler.read()
# # content1=file_handler.read(5)
# # Reset cursor back to the start of the file
file_handler.seek(0)
line1=file_handler.readline()
line2=file_handler.readline()
line3=file_handler.readline()
line4=file_handler.readline()



file_handler.close()

# print(content)
# print(content1)

print(f"Line 1 : {line1}")
print(f"Line 2 : {line2}")
print(f"Line 3 : {line3}")
print(f"Line 4 : {line4}")

