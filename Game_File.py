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
def distanceairport():
    icaoCodes = []
    for i in range(0,2):
        icao = input(f"Enter area code {i+1}: ")
        icaoCodes.append(icao)
    sql3 = "SELECT latitude_deg, longitude_deg FROM airport"
    sql3 += " WHERE ident = '" + icaoCodes[0] + "' OR ident = '" + icaoCodes[1] + "'"
    cus.execute(sql3)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        location = []
        for lat, long in row:
            location.append(lat)
            location.append(long)
        distance = geodesic((location[0],location[1]),(location[2],location[3]))
        print(f"Distance between these two airport is: {distance}")

# Function to convert km to fuel:
def convertkmtofuel(distance):
    fuelUsage = distance*12
    return fuelUsage
# Function to display variables after:
def updateVar():
    fuel = fuel - fuelUsage
    print(fuel)
    totalDistance = totalDistance + distanceTraveled
    print(totalDistance)
    print(countryTraveled)

#Game code
while countryTraveled < countryGoal:
    userName = input("Please enter your name: ")
    print(f"Hello {userName}, welcome to our flight game!\nYour goal is to visit 5 different countries without running out of fuel.\nYou have been given 20 000 liters of fuel, and will be given the oportunity to gain more later by answering trivia qustions.\nHave fun and good luck! :)")
    updateVar()