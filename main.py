import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_mk10'
)


def print_hi():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT namapelajar FROM pelajar')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])

    sql = "INSERT INTO pelajar (idpelajar, namapelajar) VALUES (%s, %s)"
    val = (2003, "Siti Hajar Binti Faris")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


if __name__ == '__main__':
    print_hi()
