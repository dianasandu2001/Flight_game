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
    Questions = ["Romania has the largest salt mine in Europe.", "Iceland doesn’t have mosquitos.", "Norway knighted a penguin. More than once.", "Wales has more sheep than people.", "It is illegal to take a picture of the Eiffel Tower.", "More than 200 Languages are spoken throughout Europe.", "The Stonehenge is the most visited attraction in Europe.", "French fries were Invented in Belgium.", "No Cappuccino After 11 Am in Italy. (social stigma)", "Spain produces 60% of Europe’s cheese.", "Of the British Museum's Collection, Only 1% Is on Display.", "It Is Illegal to Name Your Pig Napoleon in France.", "The Grand Canal in Venice is 50% wine", "Finland has the second most amount of lakes in Europe", "More Chocolate Is Bought at Brussels Airport Than Any Other Place in the World.", "Germany's Famous Oktoberfest Is Actually in November.", "80% of Greece is made up of mountains.", "Sweden is home of the first Christmas tree.", "The Danish language has no word for 'please'.", "LEGO was invented by a Russian."]
    Answers = ["true", "true", "true", "true", "false", "true", "false", "true", "true", "false", "true", "true", "false", "false", "true", "false", "true", "false", "true", "false"]

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
    number = random.randint(0, (len(Questions) - 1))
    print(Questions[number])
    answer = input("Is this true or false: ").lower()
    if answer == Answers[number]:
        # fuel = fuel + 5000
        print("Answer is correct, 5000l of fuel awarded.")
    else:
        print("Answer is wrong, no fuel awarded.")
    Questions.pop([number])
    updateVar(fuel,totalDistance)
    countryDestination = input("Which country would you like to go to next?: ")
    #filter out 3 choices of airports for the country
    airportDestination = input(f"{}this is the filtered\nWhich airpot would you like to visit in {countryDestination}: {}")
    break