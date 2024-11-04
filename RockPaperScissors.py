import random

def main ():
    print("\n")
    print("**********************************************************************************")
    print("                                    Welcome to                                    \n")
    print("                    R O C K   P A P E R   &   S C I S S O R S                     \n")
    print("  ------------------------------------------------------------------------------  \n")
    print("Instructions:")
    print("  1. Type 'r' for 'rock', 'p' for 'paper' or 's' for 'scissors' to make your move.")
    print("  2. Type 'x' to end the game.")
    print("  3. You will see the game result after each round.")
    print("  4. Let's see who wins !\n")
    print("**********************************************************************************\n")
    
    while(True):
        userChoice = input("Enter your choice (r/p/s or x) : ").lower()

        while userChoice not in ["r", "p", "s", "x"]:
            print("Invalid input. Please choose 'r', 'p', 's' or 'x'.\n")
            userChoice = input("Enter your choice (r/p/s or x) : ").lower()

        if userChoice == "x":
            print("\nExiting the game. Goodbye!")
            break
        compChoice = random.choice(["r", "p", "s"])
        print(f"\nYou chose: {userChoice}")
        print(f"Computer chose: {compChoice}\n")
        result = showWinner(userChoice, compChoice)
        print(result)
        print("\n**********************************************************************************\n")
    
    print("\n***********************************************************************************\n")
    return 0;

def showWinner(userChoice, compChoice):
    if userChoice == compChoice:
        return "  ----- It's a tie ! -----  "
    elif (userChoice == "r" and compChoice == "s") or \
         (userChoice == "p" and compChoice == "r") or \
         (userChoice == "s" and compChoice == "p"):
        return "  ----- C O N G R A T U L A T I O N S  ! ! ! -----  \n \t\t  You win!"
    else:
        return "   ----- O O P S ! -----\nYou lose. The computer wins!"

main()        