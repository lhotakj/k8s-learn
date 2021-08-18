import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python! v2"

@app.route("/db")
def database():

    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password",
        database="")

    mycursor = mydb.cursor()

    mycursor.execute("Show databases;")

    myresult = mycursor.fetchall()

    result = ''
    for x in myresult:
        result = result + str(x) + "\n"

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0')
