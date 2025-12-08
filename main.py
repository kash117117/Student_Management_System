import sys
import os
from models.manager import SystemManager #this imports the SystemManager class from the models.manager module

def print_menu(): #This is the main menu of the Student Management System
    print("\n--- Student Management System ---") 
    print("1. Add Student")
    print("2. Add Subject")
    print("3. Enroll Student")
    print("4. Add Grade")
    print("5. Mark Attendance")
    print("6. View Student Report")
    print("7. View All Students")
    print("8. Exit")
    print("---------------------------------")

def wait_for_user(): #Asks for user input
    input("\nPress Enter to return to the menu...")

def main():
    manager = SystemManager() #Accessing the SystemManager class

    while True: #creates loop
        print_menu() #entry point to the menu function
        choice = input("Enter your choice: ").strip()

        if choice == '1': #if/elif structure to navigate through the menu options
            manager.add_student()
            wait_for_user()
        elif choice == '2':
            manager.add_subject()
            wait_for_user()
        elif choice == '3':
            manager.enroll_student()
            wait_for_user()
        elif choice == '4':
            manager.add_grade()
            wait_for_user()
        elif choice == '5':
            manager.mark_attendance()
            wait_for_user()
        elif choice == '6':
            manager.view_student_report()
            wait_for_user()
        elif choice == '7':
            manager.view_all_students()
            wait_for_user()
        elif choice == '8':
            manager.save_data() #exits the system and saves data
            print("Now exiting system")
            sys.exit() 
        else:
            print("Invalid choice. Please enter a number from the options listed between 1 and 8.")
            wait_for_user()

if __name__ == "__main__": 
    main()