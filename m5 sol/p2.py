import sqlite3
MyBooks=sqlite3.connect('books.db')
curbooks=MyBooks.cursor()
btitle=input("enter the title of the book")
curbooks.execute("select * from book where Title=="+"'"+ btitle +"';")
record1=curbooks.fetchone()  #this is a tuple of values

print (record1)  #last element is the price

price = record1[-1]   #returns last element
num=int(input("no. of copies: "))

print(num*price)
