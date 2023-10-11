# Connection to DataBase
import mysql.connector
from geopy.distance import geodesic as GD
import random

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='kim',
        password='pass_word'
)
cus = connection.cursor()

# Variable
fuel = 30_000
fuelUsage = 0
totalDistance = 0
countryTravelled = 0
countryGoal = 5
currentID = '2307'
visitedCountries = []

# Lists
ID_checker = []
Questions = ["Romania has the largest salt mine in Europe.", "Iceland doesn’t have mosquitos.", "Norway knighted a penguin. More than once.", "Wales has more sheep than people.", "It is illegal to take a picture of the Eiffel Tower.", "More than 200 Languages are spoken throughout Europe.", "The Stonehenge is the most visited attraction in Europe.", "French fries were Invented in Belgium.", "No Cappuccino After 11 Am in Italy. (social stigma)", "Spain produces 60% of Europe’s cheese.", "Of the British Museum's Collection, Only 1% Is on Display.", "It Is Illegal to Name Your Pig Napoleon in France.", "The Grand Canal in Venice is 50% wine", "Finland has the second most amount of lakes in Europe", "More Chocolate Is Bought at Brussels Airport Than Any Other Place in the World.", "Germany's Famous Oktoberfest Is Actually in November.", "80% of Greece is made up of mountains.", "Sweden is home of the first Christmas tree.", "The Danish language has no word for 'please'.", "LEGO was invented by a Russian."]
Answers = ["true", "true", "true", "true", "false", "true", "false", "true", "true", "false", "true", "true", "false", "false", "true", "false", "true", "false", "true", "false"]

# Retrieve countries in Europe from database
EuropeCountries = []
sql = "SELECT name FROM country where continent = 'EU'"
cus.execute(sql)
row = cus.fetchall()
for cou in row:
    (country,) = cou
    EuropeCountries.append(country)


# Function to calculate distance between 2 airports
def distanceairport(currentID, destinationID):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE id = '" + currentID + "' OR id = '" + destinationID + "'"
    cus.execute(sql)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        location = []
        for lat, long in row:
            location.append(lat)
            location.append(long)
        dist = GD((location[0], location[1]), (location[2], location[3]))
        disArr = (str(dist)).split()
        dis = float(disArr[0])
        distance = int(dis)
        return distance

# Function to convert km to fuel:
def convertkmtofuel(distance):
    fuelUsage = distance*12
    return fuelUsage


# Function to display variables after:
def displayvar():
    print(f"\nFuel left: {fuel} litres\nDistance travelled: {totalDistance} km\nCountries travelled: {countryTravelled}")

# Function to filter 3 random airports from chosen country
def random3airport(country):
    sql = "SELECT airport.name, id FROM airport, country"
    sql += " WHERE airport.iso_country = country.iso_country AND country.name ='" + country + "' ORDER BY RAND( )  LIMIT 3"
    cus.execute(sql)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        for airport, id in row:
            print(f"Airport name: {airport} - ID: {id} ")
            ID_checker.append(str(id))

#Game code
#Intro
userName = input("Please enter your name: ")
print(f"\nHello {userName}, welcome to our flight game!\nYour goal is to visit 5 different countries without running out of fuel. Your starting point is Helsinki Vantaa Airport, Finland.\nYou have been given 30 000 liters of fuel, and will be given the opportunity to gain more later by answering trivia qustions.\nHave fun and good luck! :)")
displayvar()

#Loop
while countryTravelled < countryGoal:
    countryDestination = (input("\nWhich country would you like to go to (in Europe)?: ")).title()

    # Check if country name is correct and not duplicated
    if countryDestination in EuropeCountries:
        print()
        random3airport(countryDestination)
        destinationID = input(f"\nWhich airport would you like to visit in {countryDestination} (input ID): ")

        # Check for match ID
        while True:
            if destinationID in ID_checker:
                break
            else:
                destinationID = input("Invalid ID. Try again: ")

        # Calculate distance and convert to fuel usage
        distanceTravelled = distanceairport(currentID, destinationID)
        totalDistance += distanceTravelled
        currentID = destinationID
        fuelUsage = convertkmtofuel(distanceTravelled)
        fuel = fuel - fuelUsage
        countryTravelled += 1

        # Trivia question
        number = random.randint(0, (len(Questions) - 1))
        print("Trivia: " + Questions[number])
        answer = input("Is this true or false: ").lower()
        print()
        if answer == Answers[number]:
            fuel = fuel + 10000
            print("Answer is correct, 10000l of fuel awarded.")
            print()

            # Check if there's any fuel left
            if fuel <= 0:
                break
            print(f"You have arrived in {countryDestination}")
        else:
            print("Answer is wrong, no fuel awarded.")
            if fuel <= 0:
                break
            print(f"You have arrived in {countryDestination}")

        # Remove asked question, selected country and empty ID list
        Questions.pop(number)
        Answers.pop(number)
        visitedCountries.append(EuropeCountries.pop(EuropeCountries.index(countryDestination)))
        ID_checker = []

        # Display fuel, distance and countries travelled
        displayvar()
    else:
        if countryDestination in visitedCountries:
            print(f"Already visited {countryDestination}, try another country.")
        else:
            print("Invalid country name.")

if countryTravelled == countryGoal:
    print("\nCongratulations! You have successfully travelled to 5 different countries :)")
elif fuel <= 0:
    print("Game over :( \nYou have ran out of fuel.......The plane CRASHED!!!!!")
