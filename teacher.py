class Teacher():
    def teach(self ):
        print("Teacher is teaching")
class School(Teacher):
    def __init__(self,new_teacher):
        self.teacher = new_teacher
    def start(self):
        self.teacher.teach()
myteacher = Teacher()
myschool = School(myteacher)


