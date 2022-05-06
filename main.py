import mysql.connector

# code connect from mysql 
concetion = mysql.connector.connect(
    host="localhost",
    user="root",
    database='sistema_login',
)

# using command mysql
cursor = concetion.cursor()
