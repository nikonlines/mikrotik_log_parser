import mysql.connector

#-----------------------------

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

print("--- Show connect to DB status ---")
print(mydb)
print("done.")


print("--- Show list DB ---")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
print("done.")

print("--- Create DB ---")
try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE logs_db")
    print("done.")
except mysql.connector.Error as e:
    print(e)

print("--- Create tables ---")
try:
    mycursor = mydb.cursor()
    mycursor.execute("USE logs_db")
    mycursor.execute("""
    CREATE TABLE input (
      id INT AUTO_INCREMENT PRIMARY KEY,
      DateTime VARCHAR(20),
      DeviceName VARCHAR(50),
      In_ VARCHAR(20),
      Out_ VARCHAR(20),
      src_mac VARCHAR(20),
      Protocol VARCHAR(5),
      src_ip VARCHAR(20),
      src_port VARCHAR(10),
      dst_ip VARCHAR(20),
      dst_port VARCHAR(10),
      len VARCHAR(10)
    )
    """)

    mycursor.execute("""
    CREATE TABLE forward (
      id INT AUTO_INCREMENT PRIMARY KEY,
      DateTime VARCHAR(20),
      DeviceName VARCHAR(50),
      In_ VARCHAR(20),
      Out_ VARCHAR(20),
      src_mac VARCHAR(20),
      Protocol VARCHAR(5),
      src_ip VARCHAR(20),
      src_port VARCHAR(10),
      dst_ip VARCHAR(20),
      dst_port VARCHAR(10),
      len VARCHAR(10)
    )
    """)

    mycursor.execute("""
    CREATE TABLE output (
      id INT AUTO_INCREMENT PRIMARY KEY,
      DateTime VARCHAR(20),
      DeviceName VARCHAR(50),
      In_ VARCHAR(20),
      Out_ VARCHAR(20),
      Protocol VARCHAR(5),
      src_ip VARCHAR(20),
      src_port VARCHAR(10),
      dst_ip VARCHAR(20),
      dst_port VARCHAR(10),
      len VARCHAR(10)
    )
    """)

    print("done.")
except mysql.connector.Error as e:
    print(e)
