correctpassword="Python"
while True:
    userpassword=input("Enter the password from user")
    if(correctpassword==userpassword):
        print("Congrats ! you are welcome")
        break;
    else:
        print("OOPS! invalid password Please try again")

print("You are logged in")