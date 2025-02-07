# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:44:01 2025

@author: madel
"""

# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        """View all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

    def mark_completed(self, task_number):
        """Mark a specific task as completed."""
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return
        self.tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")

    def delete_task(self, task_number):
        """Delete a specific task from the list."""
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return
        deleted_task = self.tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['task']}' deleted.")


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task description: ")
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)

        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)

        elif choice == "5":
            print("Exiting the To-Do List program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
