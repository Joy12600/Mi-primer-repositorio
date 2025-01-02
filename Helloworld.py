class Calculator:
    def __init__(self):
        self.history = []

    def printCalculator(self):
        print("Welcome to the Calculator!")

    def addition(self, num1, num2):
        result = num1 + num2
        self.history.append(f"Addition of {num1} and {num2} is {result}")
        return result

    def subtraction(self, num1, num2):
        result = num1 - num2
        self.history.append(f"Subtraction of {num1} and {num2} is {result}")
        return result

    def multiplication(self, num1, num2):
        result = num1 * num2
        self.history.append(f"Multiplication of {num1} and {num2} is {result}")
        return result

    def division(self, num1, num2):
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return None
        result = num1 / num2
        self.history.append(f"Division of {num1} by {num2} is {result}")
        return result

    def show_history(self):
        if not self.history:
            print("No operations performed yet.")
        else:
            print("History of operations:")
            for record in self.history:
                print(record)

    def start(self):
        self.printCalculator()
        while True:
            print("\nSelect an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Show History")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            elif choice == 5:
                self.show_history()
                continue
            elif choice in [1, 2, 3, 4]:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input! Please enter valid numbers.")
                    continue

                if choice == 1:
                    print(f"Result: {self.addition(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {self.subtraction(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {self.multiplication(num1, num2)}")
                elif choice == 4:
                    result = self.division(num1, num2)
                    if result is not None:
                        print(f"Result: {result}")
            else:
                print("Invalid choice! Please select a valid option.")


# Ejecutar la calculadora
calculator = Calculator()
calculator.start()
