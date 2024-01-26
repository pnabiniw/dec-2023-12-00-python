from read import read_student
from create import create_student
from update import update_student
from delete import delete_student


def main():
    choice = input("Enter your choice (c/r/u/d/e) ")

    def exit_message():
        print("Thank you. See you again !")

    if choice == "c":
        cont = create_student()
        main() if cont else exit_message()
    elif choice == "r":
        cont = read_student()
        main() if cont else exit_message()
    elif choice == "u":
        cont = update_student()
        main() if cont else exit_message()
    elif choice == "d":
        cont = delete_student()
        main() if cont else exit_message()
    else:
        exit_message()


main()
