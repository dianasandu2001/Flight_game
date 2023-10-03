
# Function to calculate distance:
from geopy import geodisc
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

def random3airport(country):
    sql = "SELECT airport.name, ident FROM airport, country"
    sql += " WHERE airport.iso_country = country.iso_country AND country.name ='" + country + "  ORDER BY RAND ( )  LIMIT 3"
    cus.execute(sql)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        for airport, icao in row:
            print(f"Airport name: {airport} \nICAO: {icao}")

