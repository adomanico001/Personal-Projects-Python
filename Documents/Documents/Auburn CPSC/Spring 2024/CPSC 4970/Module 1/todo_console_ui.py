# This interactive program manages a to-do list.
#
# Module 1 Project
# @author Addie Domanico - CPSC 4970 - AO3
# @version 03/17/2024

import datetime

# Initialize an empty list to store to-do items
todo_list = []

while True:
    # Display main menu options
    print("\n\nMain menu:")
    print("1) List ALL todo items")
    print("2) List all incomplete todo items")
    print("3) List incomplete items due today")
    print("4) Add a todo item")
    print("5) Complete a todo item")
    print("6) Quit")

    choice = input("Enter your choice> ")

    # Option 1 - List all to-do items
    if choice == "1":
        print("\nAll items:")
        for todo in todo_list:
            completed, description, due_date = todo
            status = "complete" if completed else "incomplete"
            print(f"\t{description} due {due_date} ({status})")

    # Option 2 - List all incomplete to-do items
    elif choice == "2":
        print("\nIncomplete items:")
        for todo in todo_list:
            completed, description, due_date = todo
            if not completed:
                print(f"\t{description} due {due_date}")

    # Option 3 - List incomplete items due today
    elif choice == "3":
        print("\nIncomplete items due today:")
        today = datetime.datetime.now().date()
        for todo in todo_list:
            completed, description, due_date = todo
            if not completed and due_date.date() == today:
                print(f"\t{description} due {due_date}")

    # Option 4 - Add a new to-do item to the list
    elif choice == "4":
        description = input("\nEnter item description: ")
        due_date_str = input("Enter due date/time (MM/DD/YYYY hh:mm): ")
        due_date = datetime.datetime.strptime(due_date_str, "%m/%d/%Y %H:%M")
        todo_list.append((False, description, due_date))
        print("Added")

    # Option 5 - Complete a to-do item from the list
    elif choice == "5":
        incomplete_items = False
        for i, todo in enumerate(todo_list):
            completed, description, due_date = todo
            if not completed:
                if not incomplete_items:
                    print("\nIncomplete items:")
                    incomplete_items = True
                print(f"\t{i}) {description} due {due_date}")
        if not incomplete_items:
            print("\nNo incomplete todo items available.")
        else:
            index = int(input("Enter item to complete: "))
            if 0 <= index < len(todo_list) and not todo_list[index][0]:
                completed_item = todo_list[index]
                # Create a new tuple for the completed items
                update_item = (True, completed_item[1], completed_item[2])
                todo_list[index] = update_item
                print(f"Completed {completed_item[1]}")

    # Option 6 - Quits the program
    elif choice == "6":
        print("\nBye!")
        break
