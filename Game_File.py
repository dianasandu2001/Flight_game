"""
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
"""
#Variable
fuel = 20_000
totalDistance = 0
distanceTraveled = 0
countryTraveled = 0
countryGoal = 5

#Functions

#Game code
while countryTraveled < countryGoal:
    userName = input("Please enter your name: ")
    print(f"Hello {userName}, welcome to our flight game!\nYour goal is to visit 5 different countries without running out of fuel.\nYou have been given 20 000 liters of fuel, and will be given the oportunity to gain more later by answering trivia qustions.\nHave fun and good luck! :)")
    updateVar()