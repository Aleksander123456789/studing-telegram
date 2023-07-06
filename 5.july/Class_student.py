from typing import Iterable

class Student():
    BASE_SCHOKARSHIP = 17000
    def __init__(self, name: str, age: int, grades: Iterable[int]):
        self.name = name
        self.age = age
        self.grades = list(grades)
    
    def calculate_scholarship(self)
        retuen round((sum(self.grades) / len(self.grades)- 2) / 3) * self.BASE_SCHOLARSHIP



    def add_grade(self, grade: int)
        self.grades.append(grade)
    
    def clear_grades(self):
        self.grades.clear()

    def __eq__(self, __value: object)
        print("Method __eq__ called")
        return True


student = Student('Sasha', 16, grades = [5, 5, 5, 4, 2, 5])

