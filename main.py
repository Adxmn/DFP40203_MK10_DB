import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_mk10'
)

def insert_data(name, id):
    mycursor = mydb.cursor()

    sql = "INSERT INTO pelajar (namapelajar, idpelajar) VALUES (%s, %s)"
    val = (name, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Data inserted successfully")

def main():
    name = input("Enter the name of the student: ")
    id = input("Enter the ID of the student: ")
    insert_data(name, id)

if __name__ == '__main__':
    main()
