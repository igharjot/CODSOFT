def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ND"
    return x / y

def main():
    while True:
        print("\n***********************************************")
        print("             C A L C U L A T O R        ")
        print("***********************************************")
        print("\nSelect an operation : \n")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EXIT")
        choice = int(input("\nEnter your choice : "))

        if choice == 5:
            print("\nExiting the calculator!\n")
            break

        if choice in (1, 2, 3, 4):
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                print("")
            except ValueError:
                print("Invalid input!")
                continue

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == 3:
                print(num1, "x", num2, "=", multiply(num1, num2))

            elif choice == 4:
                result = divide(num1, num2)
                if result == "ND":
                    print("Division by zero is not defined.")
                else:    
                    print(num1, "/", num2, "=", result)

            print("\n")

        else:
            print("Invalid input! Enter your choise again.")

    print("***********************************************\n")        

main()