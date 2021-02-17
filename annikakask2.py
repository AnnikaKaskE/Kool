import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

mydb = mysql.connector.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"
)

sql = "DROP TABLE IF EXISTS Customer"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE Customer (name VARCHAR(255), address VARCHAR(255), dob DATE, card_number VARCHAR(16), pin VARCHAR(4) )")
sql = "DROP TABLE IF EXISTS Bank"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE Bank (code VARCHAR(255), address VARCHAR(255), revenue FLOAT )")
sql = "DROP TABLE IF EXISTS Account"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE Account (number FLOAT, balance FLOAT)")
sql = "DROP TABLE IF EXISTS ATM"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE ATM (location FLOAT, managedby VARCHAR(255))")
sql = "DROP TABLE IF EXISTS ATM_Transactions"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE ATM_Transactions (transaction_id VARCHAR(255), date DATE, type VARCHAR(255), amount FLOAT, post_balance FLOAT )")
sql = "DROP TABLE IF EXISTS CurrentAccount"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE CurrentAccount (account_no VARCHAR(255), balance FLOAT, interet_rate FLOAT )")
sql = "DROP TABLE IF EXISTS SavingAccount"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE SavingAccount (account_no VARCHAR(255), balance FLOAT, credit_range FLOAT )")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


mycursor.execute("ALTER TABLE Customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE Bank ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE Account ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE ATM ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE ATM_Transactions ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE CurrentAccount ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE SavingAccount ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO Customer (name, address, dob, card_number) VALUES (%s, %s, %s, %s)"
val = [
('Peter', 'Lowstreet 4', '15.06.2000', '111111111111'),
('Amy', 'Apple st 652', '15.06.2000', '111111111112'),
('Hannah', 'Mountain 21', '15.06.2000', '111111111113'),
('Michael', 'Valley 345', '15.06.2000', '111111111114'),
('Sandy', 'Ocean blvd 2', '15.06.2000', '111111111115'),
('Betty', 'Green Grass 1', '15.06.2000', '111111111116'),
('Richard', 'Sky st 331', '15.06.2000', '111111111117'),
('Susan', 'One way 98', '15.06.2000', '111111111118'),
('Vicky', 'Yellow Garden 2', '15.06.2000', '111111111119'),
('Ben', 'Park Lane 38', '15.06.2000', '111111111120'),
('William', 'Central st 954', '15.06.2000', '111111111121'),
('Chuck', 'Main Road 989', '15.06.2000', '111111111122'),
('Viola', 'Sideway 1633', '15.06.2000', '111111111123')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM Customer")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
