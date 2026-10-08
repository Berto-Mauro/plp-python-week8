import random


# This function performs addition, subtraction, multiplication, and division.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    while True:
        try:
            first_number = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            second_number = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        operation = input("Enter your choice: ").strip()

        if operation == "1":
            answer = first_number + second_number
            print(f"\nThe answer is {answer}.")
            break

        elif operation == "2":
            answer = first_number - second_number
            print(f"\nThe answer is {answer}.")
            break

        elif operation == "3":
            answer = first_number * second_number
            print(f"\nThe answer is {answer}.")
            break

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                answer = first_number / second_number
                print(f"\nThe answer is {answer}.")
                break

        else:
            print("Invalid operation. Please choose 1, 2, 3, or 4.")


# This function allows the user to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task == "":
                print("You cannot add an empty task.")
            else:
                tasks.append(task)
                print(f"Task '{task}' has been added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                while True:
                    try:
                        task_number = int(
                            input("Enter the task number to remove: ")
                        )
                        break
                    except ValueError:
                        print("Please enter a whole number.")

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' has been removed.")
                else:
                    print("That task number does not exist.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 4.")


# This function creates a number guessing game.
def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")

    secret_number = random.randint(1, 10)
    attempts = 0

    print("I have chosen a number between 1 and 10.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 10:
            print("Please choose a number between 1 and 10.")
            continue

        attempts = attempts + 1

        if guess < secret_number:
            print("Your guess is too low.")

        elif guess > secret_number:
            print("Your guess is too high.")

        else:
            print(
                f"Congratulations! You guessed the number "
                f"in {attempts} attempts."
            )
            break


# This function formats the user's name and gives a friendly greeting.
def name_formatter():
    print("\n--- NAME FORMATTER ---")

    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if first_name == "" or last_name == "":
        print("Please enter both your first name and last name.")
        return

    full_name = f"{first_name.title()} {last_name.title()}"

    print(f"\nYour formatted name is: {full_name}.")
    print(f"Welcome, {full_name}!")


# This is the main menu of the program.
print("==========================================")
print("   WELCOME TO MY PERSONAL MINI-TOOLKIT")
print("==========================================")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        name_formatter()

    elif choice == "5":
        print("\nThank you for using My Personal Mini-Toolkit!")
        print("Goodbye! Have a great day!")
        break

    else:
        print(f"\nSorry, '{choice}' is not a valid choice.")
        print("Please choose a number from 1 to 5.")
        
        
        
        