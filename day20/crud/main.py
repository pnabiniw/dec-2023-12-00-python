from read import read_student
from create import create_student
from update import update_student
from delete import delete_student


def main():
    choice = input("Enter your choice (c/r/u/d/e) ")

    def exit_message():
        print("Thank you. See you again !")

    if choice == "c":
        create_student()
    elif choice == "r":
        read_student()
    elif choice == "u":
        update_student()
    elif choice == "d":
        delete_student()
    else:
        exit_message()


main()
