# -*- coding: utf-8 -*-
class Student1:
    name = "Jonas"
    grades = ["5a", "4c", "5b", "3d", "5a"]

    def greeetings(self):
        hello = f'Привіт, мене звати {self.name}.'
        return hello

    def grade_list(self):
        self.grades = ", ".join(self.grades)
        intro_grade = f'Мої оцінки: {self.grades}'
        return intro_grade


obj_student1 = Student1()
obj_student2 = Student1()
obj_student2.name = "Viacheslav"
print(f'{obj_student1.greeetings()}\n{obj_student1.grade_list()}')
print()
print(f'{obj_student2.greeetings()}\n{obj_student2.grade_list()}')
