from entity.student import Student


class BaseService:

    students = []

    @classmethod
    def add_student(cls):
        roll_no = input('Roll No. : ')
        first_name = input('First name :  ')
        last_name = input('Last name :  ')
        f_name = input('Father\'s name :  ')
        m_name = input('Mother\'s name :  ')
        email = input('Email :  ')
        phone = int(input('Phone number :  '))
        s_class = int(input('Class :  '))
        section = input('Section :  ')
        new_student = Student(roll_no, first_name, last_name, f_name, m_name, email, phone, s_class, section)
        cls.students.append(new_student)
        print('{} {}\'s record added successfully!!!'.format(new_student.first_name, new_student.last_name))

    @classmethod
    def display_all_records(cls):
        if cls.students:
            for student in cls.students:
                print(student)
        else:
            print('No records added yet. Please add records!!!')

    @classmethod
    def update_record(cls):
        roll_no = input('Roll No. : ')
        for idx, student in enumerate(cls.students):
            if student.roll_no == roll_no:
                first_name = input('First name :  ')
                last_name = input('Last name :  ')
                f_name = input('Father\'s name :  ')
                m_name = input('Mother\'s name :  ')
                email = input('Email :  ')
                phone = int(input('Phone number :  '))
                s_class = int(input('Class :  '))
                section = input('Section :  ')
                new_student = Student(roll_no, first_name, last_name, f_name, m_name, email, phone, s_class, section)
                cls.students[idx] = new_student
                print('Student record successfully updated!!!')
                break

    @classmethod
    def remove_student(cls):
        roll_no = input('Roll No. : ')
        for idx, student in enumerate(cls.students):
            if student.roll_no == roll_no:
                cls.students.pop(idx)
                break
        print('Student record successfully deleted!!!')
