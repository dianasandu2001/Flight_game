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
import random

#Variable
fuel = 20_000
fuelUsage = 0
totalDistance = 0
distanceTraveled = 0
countryTraveled = 0
countryGoal = 5

#Lists
    Questions = ["Romania is the largest salt mine in Europe", ]
    Answers = ["true", ]

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
        return distance

# Function to convert km to fuel:
def convertkmtofuel(distance):
    fuelUsage = distance*12
    return fuelUsage
# Function to display variables after:
def updateVar(fuel, totalDistance):
    fuel = fuel - fuelUsage
    print(f"Your remaining fuel is: {fuel}l")
    distanceTraveled = distanceairport()
    totalDistance = totalDistance + distanceTraveled
    print(f"You have travelled: {totalDistance}km")
    print(f"Countries travelled to: {countryTraveled}")
#Function to filter 3 random airports from chosen country
def random3airport(country):
    sql = "SELECT airport.name, ident FROM airport, country"
    sql += " WHERE airport.iso_country = country.iso_country AND country.name ='" + country + "  ORDER BY RAND ( )  LIMIT 3"
    cus.execute(sql)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        for airport, icao in row:
            print(f"Airport name: {airport} \nICAO: {icao} ")

#Game code
userName = input("Please enter your name: ")
print(f"Hello {userName}, welcome to our flight game!\nYour goal is to visit 5 different countries without running out of fuel.\nYou have been given 20 000 liters of fuel, and will be given the oportunity to gain more later by answering trivia qustions.\nHave fun and good luck! :)")
updateVar(fuel, totalDistance)
countryDestination = input("Which country would you like to go to (in Europe)?: ")
#filter out 3 choices of airports for the country
airportDestination = input(f"{}this is the filtered\nWhich airpot would you like to visit in {countryDestination}: {}")
while countryTraveled < countryGoal:
    #ask the question
    number = random.randint(0, (len(Questions)-1))
    print(random.choice(Questions))
    answer = lower.input("Is this true or false: ")
        if answer in Answers:
            fuel = fuel + 5000
            print("Answer is correct, 5000l of fuel awarded")
        else:
            print("Answer is wrong, no fuel awarded")
    updateVar(fuel,totalDistance)
    countryDestination = input("Which country would you like to go to next?")
    #filter out 3 choices of airports for the country
    airportDestination = input(f"{}this is the filtered\nWhich airpot would you like to visit in {countryDestination}: {}")
    break