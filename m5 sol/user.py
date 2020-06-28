#To calculate the total cost as per the required no. of books
import sqlite3
MyBooks=sqlite3.connect('books.db')
curbooks=MyBooks.cursor()
total=0
while True:
    btitle=input("Book Title: ")
    curbooks.execute("select * from book where Title=="+"'"+ btitle +"';")
    
    record1=curbooks.fetchone()
    if record1==None:
        print("Book not found")
        break
    print (record1)

    num=int(input("No. of copies : "))
    curbooks.execute("select Price from book where Title=="+"'"+btitle+"';")
    while True:
        record2=curbooks.fetchone()
        if record2==None:
            break
        p=int(record2[0])
        total=total+(num*p)
    s=input("Add more books? Y/N ")
    if s=='N':
        break
    


print("Total Cost : ", total)

