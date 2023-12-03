class Library:
    no_of_books=0
    bookslist=[""]
    bookname=""
    
    def add(self):
        self.no_of_books+=1
        self.bookname= input("Enter the name of book")
        self.bookslist.append(self.bookname)
        print (f"{self.bookname} added successfully\n")
    def print(self):
        for book in self.bookslist:
         
          print(f"    {book}\n")
    def shownumofbooks(self):
        print (" Total Number of Books in library:",self.no_of_books)
    def checkbookserror(self):
        if not self.no_of_books==len(self.bookslist):
            print("Error has occured :Books are Missing")
library1= Library()
print("\nWELCOme TO Library Management System\n")
x=True
while x==True:
        print(" 1.Browse Library i.e list all books\n 2.Add a new book in library\n 3.See total numbers of book\n 4.check for an error if there is\n  Press any other key to exit")
        choice=int(input())
        if choice==1:
            print("List of all books in the Library are: \n")
            library1.print()
        elif choice==2:
            library1.add()
        elif choice==3:
            library1.shownumofbooks()
        elif choice==4:
            library1.checkbookserror()
        else:
            x=False




