def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0:
        return "Error. Can't divide by zero."
    return x / y

def menu():
    print("Choose an operation")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Divide")


while True:
    menu()
    user_choice = input("")
    if user_choice in ('1', '2', '3', '4'):
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if user_choice == '1':
            print(add(x,y))
        elif user_choice == '2':
            print(subtract(x,y))
        elif user_choice == '3':
            print(multiply(x,y))
        elif user_choice == '4':
            print(divide(x,y))
        again = input("Do you want to do another operation? y/n : ")
        if again.upper()=="N":
            break
    else:
        print("Invalid Choice. Please enter 1, 2, 3, or 4.")
