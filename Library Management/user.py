import getpass
import pickle

class user:      
    def student_reg(self):
        with open("studentlist.pkl","rb") as f:
            self.name=input("Enter Student Name:")
            self.br=input("Enter Student Branch")
            while True:
                try:
                    obj=pickle.load(f)
                    for student in obj:
                        if ((student.name == self.name and student.br == self.br)):
                            return True
                except EOFError:
                    print("User doest not exist")
                    break
    def teacher_reg(self):
        with open("teacherlist.pkl","rb") as f:
            self.name=input("Enter Teacher Name:")
            self.i=input("Enter Teacher ID")
            while True:
                try:
                    obj=pickle.load(f)
                    for teacher in obj:
                        if ((teacher.name == self.name and teacher.i == self.i)):
                            return True
                except EOFError:
                    print("Teacher doest not exist")
                    break
                    
    def admin(self):
        password = getpass.getpass("Enter password :")
        if password == '1234':
            return True
        else:
            return False
        
        
            
        

