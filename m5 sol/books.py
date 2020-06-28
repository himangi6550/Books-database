import sqlite3
MyBooks=sqlite3.connect('books.db')
curbooks=MyBooks.cursor()
#creating table book
curbooks.execute('''CREATE TABLE IF NOT EXISTS BOOK(
                                  BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  Title TEXT(30) NOT NULL,
                                  Author TEXT(30),
                                  Price REAL);''')

#data to be inserted into the table
val= [ (1290,'Pride and Prejudice','Jane Austen',190),
       (1246,'Sherlock Holmes','Arthur Conan Doyle',270),
       (1387,'War And Peace','Leo Tolstoy',700),
       (1249,'David Copperfield','Charles Dickens',300),
       (1294,'Half Girlfriend','Chetan Bhagat',170),
       (1574,'One Night at Call Centre','Chetan Bhagat',140),
       (12,'The Red and the Black','Stendhal',990),
       (129,'The Blue Umbrella','Ruskin Bond',100),
       (1190,'The Alchemist','Paulo Coelho',700),
       (126,'Great Expectations','Charles Dickens',730),
       (1478,'Disgrace','John Maxwell Coetzee',500),
       (1295,'Learn C the Hard Way','Zed Shaw',1500),
       (1299,'Think Python','Alen B. Downey',550),
       (144,'Core Java','Dr. R Nageshwar Rao',500),
       (167,'Train to Pakistan','Khushwant Singh',150),
       ]
#inserting the data into the table
curbooks.executemany("INSERT INTO BOOK(BookID,Title,Author,Price) VALUES (?,?,?,?);", val)
MyBooks.commit()


