class teacher:
    def insert(self):
        self.name=input("Enter the teacher name")
        self.i=input("Enter the ID")
        self.dict={}
        self.dat=None
    def display(self):
        print(f"Name is :{self.name}\nID is:{self.i}\nMore Information :{self.dict}")