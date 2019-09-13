class book:
    def add(self):
        self.title=input('title:')
        self.author=input('Enter author:')
        self.sbin=int(input('enter its ISBN number:'))
        self.copies=int(input('enter its copies'))
    
    def display(self):
        print(f'Title of Book:  {self.title}\nThe author of book:  {self.author}\nSBIIN book:  {self.sbin}\nCopies :  {self.copies}')