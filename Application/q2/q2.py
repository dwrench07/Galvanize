#!/bin/python
"""Question 2:

Suppose we have 2 tables called Orders and Salesperson shown below:

Orders
+--------+------------+---------+----------------+--------+
| Number | order_date | cust_id | salesperson_id | Amount |
+--------+------------+---------+----------------+--------+
| 10     | 8/2/96     | 4       | 2              | 540    |
| 20     | 1/30/99    | 4       | 8              | 1800   |
| 30     | 7/14/95    | 9       | 1              | 460    |
| 40     | 1/29/98    | 7       | 2              | 2400   |
| 50     | 2/3/98     | 6       | 7              | 600    |
| 60     | 3/2/98     | 6       | 7              | 720    |
| 70     | 5/6/98     | 9       | 7              | 150    |
+--------+------------+---------+----------------+--------+

Salesperson
+----+-------+-----+--------+
| ID | Name  | Age | Salary |
+----+-------+-----+--------+
| 1  | Abe   | 61  | 140000 |
| 2  | Bob   | 34  | 44000  |
| 5  | Chris | 34  | 40000  |
| 7  | Dan   | 41  | 52000  |
| 8  | Ken   | 57  | 115000 |
| 11 | Joe   | 38  | 38000  |
+----+-------+-----+--------+

Write a SQL query that retrieves the names of all salespeople 
that have more than 1 order from the tables above. 

You can assume that each salesperson only has one ID.

"""
import sqlite3

db = sqlite3.connect(':memory:')
c = db.cursor()
print('Running SQLite Version: {}'.format(sqlite3.version))

# Create tables
c.execute("""CREATE TABLE IF NOT EXISTS Salesperson(
                          ID INT PRIMARY KEY NOT NULL,
                          Name TEXT,
                          Age INT,
                          Salary  REAL);
                          """)

c.execute("""CREATE TABLE IF NOT EXISTS Orders(
                        Number INT PRIMARY KEY NOT NULL,
                        order_date     DATE,
                        cust_id        INT,
                        salesperson_id INT,
                        Amount         INT,
                        FOREIGN KEY(salesperson_id) REFERENCES Salesperson(ID)
                        );""")
db.commit()

# Insert that sweet, sweet data
c.execute("""INSERT INTO Salesperson
             VALUES (1, 'Abe', 61, 140000),
                    (2, 'Bob', 34, 40000),
                    (5, 'Chris', 34, 40000),
                    (7, 'Dan', 41, 52000),
                    (8, 'Ken', 57, 115000),
                    (11, 'Joe', 38, 38000);
          """)

c.execute("""INSERT INTO Orders
             VALUES (10, '8/2/96', 4, 2, 540),
                    (20, '1/30/99', 4, 8, 1800),
                    (30, '7/14/95', 9, 1, 460),
                    (40, '1/29/98', 7, 2, 2400),
                    (50, '2/3/98', 6, 7, 600),
                    (60, '3/2/98', 6, 7, 720),
                    (70, '5/6/98', 9, 7, 150);
          """)
db.commit()

query = """SELECT Salesperson.Name
                     FROM Salesperson
                     INNER JOIN Orders
                     ON Salesperson.ID = Orders.salesperson_id;"""
# Finally, actually execute the query
results = c.execute(query).fetchall()

# Show what query it is we are running to the user
print('SQL query to be ran: {}'.format(query))

print('Results:')
print(set(results))
