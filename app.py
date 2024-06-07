#!/usr/bin/env python3
from calculations import sum

def get_user_input():
    while True:
        print("""
            Here are your options:
                1. Create a todo
                2. Mark a todo as done
                3. Delete a todo
                4. View all todos
                5. Find a todo by name
                6. Exit app
            """)
        option = input("Enter your option: ")
        if option == "1":
            pass # call a function to create the todo
        if option == "6":
            break

if __name__ == "__main__":
    get_user_input()