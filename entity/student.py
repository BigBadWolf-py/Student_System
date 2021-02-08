class Student:

    def __init__(self, roll_no, first_name, last_name, f_name, m_name, email, phone, s_class, section):
        self.roll_no = roll_no
        self.first_name = first_name
        self.last_name = last_name
        self.f_name = f_name
        self.m_name = m_name
        self.email = email
        self.phone = phone
        self.s_class = s_class
        self.section = section

    def __repr__(self):
        return 'Roll No.: {}\nStudent Name: {} {}\nFather\'s Name: {}\nMother\'s name: {}\nEmail: {}\nPhone: {}\n' \
               'Class: {} {}'.format(self.roll_no, self.first_name, self.last_name, self.f_name, self.m_name,
                                     self.email, self.phone, self.s_class, self.section)
