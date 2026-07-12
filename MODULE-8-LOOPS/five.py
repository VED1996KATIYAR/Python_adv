import random
print("Welcome to game of rolling a dice")
while True:
    choice=input("Press Enter to roll a dice or 'q' to quit ")
    choice=choice.strip()
    if choice=='q':
        print("Thanks for playing")
        break
    elif choice=='':
        number=random.randint(1,6)
        print(f"Your no is {number}")
    else:
        print("Invalid Input")
print("Game Over")