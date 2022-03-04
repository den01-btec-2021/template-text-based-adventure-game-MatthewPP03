def main():
    print("welcome to my game!")
    player_name=input("What is your name?")
    print("Hi" + player_name)

    lives = 3
    print(f"You have {lives} lives remaining")

    direction = input("Which direction would you like to go?")

    if direction == "North": 
        print("You have now travelled North!")
    elif direction == "South":
        print("You have travelled South!")
    elif direction == "West":
        print("You have now travelled West!")
    elif direction == "East":
        print("You have travelled East!")

main()
