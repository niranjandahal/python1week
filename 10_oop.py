class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_grade(self):
        return self.grade

class course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students) < len(self.max_students):
            self.students.append(self.student)
            return True
        return False




