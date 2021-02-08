from service.baseservice import BaseService


class StudentService:

    @classmethod
    def remove_student(cls):
        BaseService.remove_student()

    @classmethod
    def add_student(cls):
        BaseService.add_student()

    @classmethod
    def display_all_records(cls):
        BaseService.display_all_records()

    @classmethod
    def update_record(cls):
        BaseService.update_record()
