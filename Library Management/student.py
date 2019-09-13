class student:
    def add(self):
        self.name=input("Enter the student name")
        self.roll=input("Enter The enrolment No.")
        self.br=input("Enter the branch")
        self.dic={}
        self.date=None
    def disp(self):
        print(f"Name is :{self.name}\nBranch is:{self.br}\nEnrollment No.{self.roll}\nMore Information :{self.dic}")