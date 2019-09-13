import pickle
from student import * 
from teacher import *
from book import *
from user import *
import datetime
import numpy as np

student_list=[]
teacher_list=[]
book_list=[] 
u=user()  
    
def search():
    load_book()
    with open("Booklist.pkl","rb") as f:
        sbin=int(input("Enter SBIN No."))
        while True:
            try:
                obj=pickle.load(f)
                for book in obj:
                    if  book.sbin == sbin:
                            print("*"*50)
                            print("Book Available ",book.title)
                            print("No. of copies are ",book.copies)
                else:
                    print("Book not found")
            except EOFError:
                print("Search is completed")
                break
    

def add_book():
    b=len(book_list)
    if b == 0:
        with open("booklist.pkl","wb") as f:
            n=int(input("How many books to be Added"))
            for i in range(n):
                b=book()
                b.add()
                book_list.append(b)
            pickle.dump(book_list,f)
    else:
        with open("booklist.pkl","ab") as f:
            n=int(input("How many books to be Added"))
            for i in range(n):
                b=book()
                b.add()
                book_list.append(b)
            pickle.dump(book_list,f)
        
        
def load_book():
    with open("booklist.pkl",'rb') as f:
        while True:
            try:
                obj=pickle.load(f)
                for data in obj:
                    data.display()
            except EOFError:
                print("Data read is completed")
                break        
    
def add_student():
    s=len(student_list)
    if s==0:
        with open("studentlist.pkl","wb") as f:
            n=int(input("How many record to be entered"))
            for i in range(n):
                s=student()
                s.add()
                student_list.append(s)
            pickle.dump(student_list,f)
    else:
        with open("studentlist.pkl","ab") as f:
            n=int(input("How many record to be entered"))
            for i in range(n):
                s=student()
                s.add()
                student_list.append(s)
            pickle.dump(student_list,f)
        
def load_student():
    with open("studentlist.pkl",'rb') as f:
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    user.disp()
            except EOFError:
                print("Data read is completed")
                break
def add_teacher():
    t=len(teacher_list)
    if t==0:
        with open("teacherlist.pkl","wb") as f:
            n=int(input("How many record to be entered"))
            for i in range(n):
                t=teacher()
                t.insert()
                teacher_list.append(t)
            pickle.dump(teacher_list,f) 
    else:
        with open("teacherlist.pkl","ab") as f:
            n=int(input("How many record to be entered"))
            for i in range(n):
                t=teacher()
                t.insert()
                teacher_list.append(t)
            pickle.dump(teacher_list,f) 
        
def load_teacher():
    with open("teacherlist.pkl",'rb') as f:
        while True:
            try:
                obj=pickle.load(f)
                for data in obj:
                    data.display()
            except EOFError:
                print("Data read is completed")
                break    
                
def issue():
    print("Available Books are :")
    load_book()
    print("*"*50)
    if u.student_reg():
        with open("booklist.pkl","rb") as f:     
            sbin=int(input("Enter ISBN No. of book you want"))
            while True:
                try:
                    obj=pickle.load(f)
                    for book in obj:
                        if (book.sbin == sbin):
                            copy=int(input("Enter No. of copies"))
                            if book.copies > copy:
                                print("Book Issued ")
                                book.copies-=copy
                                update(copy,sbin)
                                break
                    else:
                        print("Book Cant be issued")
                        break
                except EOFError:
                    print("*"*50)
                    break
        with open("booklist.pkl","wb") as f:
            pickle.dump(obj,f)
    else:
        print("*"*50)
        
def update(copy,sbin):
    obj=None
    with open("studentlist.pkl","rb") as f:
        r=input("Enter your roll no. for verification ")
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    print("Name",user.name)
                    if user.roll == r:
                        print("Enrollment",user.roll)
                        user.dic[sbin]=copy
#                         if user.dic[sbin]:
#                             user.dic[sbin]+=copy
#                         else:
#                             user.dic[sbin]=copy
                        user.date=datetime.datetime.now().date()
                        break
            except EOFError:
                print("Data read is modified")
                break
    with open("studentlist.pkl","wb") as f:
            pickle.dump(obj,f)

def return_student():
    with open("studentlist.pkl","rb") as f:
        r=input("Enter your roll no. to return :")
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    if bool(user.dic):
                        print("Name",user.name)
                        if user.roll == r:
                            b=list(user.dic.keys())
                            c=list(user.dic.values())
                            print("SBIN of Books you have :",b)
                            print("Copies of Book you have :",c)
                            r=int(input("Enter the SBIN for the book you want to return :"))
                            val=user.dic[r]
                            pop(val,r)
                            user.dic.pop(r)
                        #user.dic.pop('Date')
                            break
                        else:
                            print("You Dont have any book")
                            break
            except EOFError:
                print("*"*50)
                break
    with open("studentlist.pkl","wb") as f:
        pickle.dump(obj,f)

def pop(val,r):
    with open("booklist.pkl","rb") as a:
        while True:
            try:
                bb=pickle.load(a)
                for book in bb:
                    if book.sbin == r:
                        book.copies+=val
                        break
            except EOFError:
                print("*"*50)
                break
    with open("booklist.pkl","wb") as a:
        pickle.dump(bb,a)
        
def fine():
    with open("studentlist.pkl","rb") as f:
        r=input("Enter your roll no. to see your fine ")
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    if bool(user.dic):
                        if user.roll == r:
                            DD = datetime.timedelta(days=30)
                            cmp= (user.date) - (datetime.datetime.now().date())
                            if cmp > DD:
                                f=list(user.dic.values())
                                for b in f:
                                    t+=f[b]
                                fine=t*10
                                print("Your Fine Till Today is :",fine)
                                break
                            else:
                                print("No Fine Till Today ")
                                break
                        else:
                            print("User Not Has this Roll")
                            break
                    else:
                        print("User has no BOOKS")
                        break
            except EOFError:
                print("*"*50)
                break
    with open("studentlist.pkl","wb") as f:
        pickle.dump(obj,f)
        
        
def issue_teacher():
    print("Available Books are :")
    load_book()
    print("*"*50)
    if u.teacher_reg():
        with open("booklist.pkl","rb") as f:     
            sbin=int(input("Enter ISBN No. of book you want"))
            while True:
                try:
                    obj=pickle.load(f)
                    for book in obj:
                        if (book.sbin == sbin):
                            copy=int(input("Enter No. of copies"))
                            if book.copies > copy:
                                print("Book Issued ")
                                book.copies-=copy
                                update_t(copy,sbin)
                                break
                    else:
                        print("Book Cant be issued")
                        break
                except EOFError:
                    print("*"*50)
                    break
        with open("booklist.pkl","wb") as f:
            pickle.dump(obj,f)
    else:
        print("*"*50)
        
def update_t(copy,sbin):
    obj=None
    with open("teacherlist.pkl","rb") as f:
        idd=input("Enter your ID for Verification ")
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    print("Name",user.name)
                    if user.i == idd:
                        print("ID",user.i)
                        user.dict[sbin]=copy
                        user.dat=datetime.datetime.now().date()
                        break
            except EOFError:
                print("Data read is modified")
                break
    with open("teacherlist.pkl","wb") as f:
            pickle.dump(obj,f)

def return_teacher():
    with open("teacherlist.pkl","rb") as f:
        r=input("Enter ID to return :")
        while True:
            try:
                obj=pickle.load(f)
                for user in obj:
                    if bool(user.dict):
                        print("Name",user.name)
                        if user.i == r:
                            b=list(user.dict.keys())
                            c=list(user.dict.values())
                            print("SBIN of Books you have :",b)
                            print("Copies of Book you have :",c)
                            r=int(input("Enter the SBIN for the book you want to return :"))
                            val=user.dict[r]
                            pop(val,r)
                            user.dict.pop(r)
                        #user.dic.pop('Date')
                            break
                        else:
                            print("You Dont have any book")
                            break
            except EOFError:
                print("*"*50)
                break
    with open("teacherlist.pkl","wb") as f:
        pickle.dump(obj,f)     
                        
                   
                    
    

        
