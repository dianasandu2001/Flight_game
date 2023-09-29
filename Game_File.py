#Connection to DataBase
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='people',
    user='dbuser',
    password='pass_word',
    autocommit=True
)

#Variable
fuel = 20_000
totalDistance = 0
distanceTraveled = 0
countryTravaled = 0
countryGoal = 5

#Functions

#Game code
while countryTravaled < countryGoal:
    woop