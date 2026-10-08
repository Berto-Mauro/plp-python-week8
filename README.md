# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a simple Python program that combines several useful tools into one menu-driven application. The program allows the user to choose different tools and return to the main menu after using each tool.

## Tools Included

The toolkit contains four tools:

* **Simple Calculator** – performs addition, subtraction, multiplication, and division.
* **To-Do List** – allows the user to add, view, and remove tasks.
* **Number Guessing Game** – allows the user to guess a randomly selected number.
* **Name Formatter** – formats the user's first and last name and gives a friendly greeting.

## Python Concepts Used

This project demonstrates several Python concepts that I learned during the course, including:

* Variables
* User input
* Output
* If, elif, and else statements
* While loops
* For loops
* Lists
* Functions
* Random numbers
* F-strings
* Error handling
* Comments

## How to Run the Program

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python toolkit.py
```

If your computer uses Python 3 through the `python3` command, run:

```bash
python3 toolkit.py
```

The program will display a menu. Enter the number of the tool you want to use. After completing a tool, the program returns to the main menu. Choose option 5 to quit.

## Screenshots

The `screenshots` folder contains screenshots showing the main menu, invalid choice handling, and each tool running.

## Reflection

The hardest part of this project was connecting all the tools to one menu while making sure the program continued running after each tool finished. I also had to understand how loops and functions work together in a menu-driven program. The bug that took the longest to fix was making sure invalid input did not cause the program to crash. I learned that using try and except can help a program handle incorrect input safely. Building the to-do list also helped me understand how a list can change while a program is running. I enjoyed seeing different Python concepts work together in one program. With one more week, I would add a simple expense tracker and save the user's tasks to a file so that the information would not disappear when the program closes.
