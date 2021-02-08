import sys
from service.studentservice import StudentService


class Menu:

    @staticmethod
    def take_input():
        option = int(input('1. Add Student record\n2. Delete Student record\n3. Display all Student records\n'
                           '4. Update Student Record  '))
        return option

    @classmethod
    def assign_func(cls, option):
        if option == 1:
            StudentService.add_student()
        elif option == 2:
            StudentService.remove_student()
        elif option == 3:
            StudentService.display_all_records()
        elif option == 4:
            StudentService.update_record()


if __name__ == '__main__':
    print('App is initialising!!!')
    while True:
        choice = Menu.take_input()
        Menu.assign_func(choice)
        while True:
            jump_back_to_menu = int(input("If you want to continue enter '1' else enter '0' "))
            if jump_back_to_menu == 1:
                break
            elif jump_back_to_menu == 0:
                print('Thanks for using the Student system!!!')
                sys.exit(1)
            else:
                print('You seem to have entered a wrong input. Please try again!!!')
