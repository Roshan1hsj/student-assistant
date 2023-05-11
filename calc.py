import webbrowser
def calculator():
    a=int(input("1.BASIC CALCULATOR \n2. GOOGLE CALCULATOR \nCHOOSE (1/2): "))
    if a==2:
        print("THE CALCULATOR WILL BE OPENED IN YOUR DEFAULT WEB BROWSER")
        webbrowser.open("https://www.google.com/search?q=google+calculator&oq=google+calculator&aqs=chrome..69i57j0i433i512j0i512l8.7785j0j7&sourceid=chrome&ie=UTF-8", new=1)
    else:
        # This function adds two numbers
        def add(x, y):
            return x + y

        # This function subtracts two numbers
        def subtract(x, y):
            return x - y

        # This function multiplies two numbers
        def multiply(x, y):
            return x * y

        # This function divides two numbers
        def divide(x, y):
            return x / y

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
            # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))

                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation in "noNONo":
                    break

            else:
                print("Invalid Input")
