# trip_calculator: This script calculates the trip of a robot through the five randomly generated meteorite sites.

#importing the needed libraries
import json
import math

#the mars radius
MARS_RADIUS = 3389.5
ROBOT_SPEED = 10

def calculate_travel_time(latitudeA: float, longitudeA: float, latitudeB: float, longitudeB: float) -> float:
    """
    This function calculates the total travel time from point A to point B
    using the great-circle distance algorithm. Then returns the total travel time.

    Args:
        latitudeA (float): The latitude of point A.
        longitudeA (float): THe longitude of point A.
        latitudeB (float): The latitude of point B.
        longitudeB (float): The longitude of point B.

    Returns:
        travelTime (float): The total travel time in hours.
    """

    #the given calculations to calculate the total travel time
    latA, lonA, latB, lonB = map(math.radians, [latitudeA, longitudeA, latitudeB, longitudeB])
    d_sigma = math.acos(math.sin(latA) * math.sin(latB) + math.cos(latA) * math.cos(latB) * math.cos(abs(lonA-lonB)))

    #returns the results
    return ((MARS_RADIUS * d_sigma) / ROBOT_SPEED)

def calculate_sample_time(composition: str) -> int:
    """
    This function returns the corresponding sampling time depending on which
    composition it is. Stony takes 1 hr, iron takes 2 hrs, and stony-iron
    takes 3 hrs.

    Args:
        composition (str): The type of composition the meteorite is.

    Returns:
        sampleTime (int): The time it takes to sample the meteorite.
    """

    #if-statements that correspond to the amount of time each composition takes to sample
    if (composition == 'stony'):
        sampleTime = 1
    elif (composition == 'iron'):
        sampleTime = 2
    elif (composition == 'stony-iron'):
        sampleTime = 3

    #returns the sample time
    return sampleTime
    
def main():
    #opening and storing the json file created
    with open('random_meteorites.json', 'r') as file:
        meteorite_data = json.load(file)    

    #the starting coordinates for the robot
    startingCoordinates = [16.0, 82.0]

    #lists to contain all the latitudes and longitudes in order
    allLatitudes = [startingCoordinates[0]]
    allLongitudes= [startingCoordinates[1]]

    #for-loop used to store the rest of the latitudes and longitudes
    for i in range(5):
        allLatitudes.append(meteorite_data['sites'][i]['latitude'])
        allLongitudes.append(meteorite_data['sites'][i]['longitude'])

    #initializing the variable for the total amount of time elapsed
    totalTime = 0.0
        
    #prints the data for each trip
    for trip in range(5):
        sampleTime = calculate_sample_time(meteorite_data['sites'][trip]['composition'])
        travelTime = calculate_travel_time(allLatitudes[trip], allLongitudes[trip], allLatitudes[trip + 1], allLongitudes[trip + 1])
        totalTime = totalTime + travelTime + sampleTime
        print(f'leg = {trip + 1}, time to travel = {travelTime:.2f} hr, time to sample = {sampleTime} hr')

    #prints the rest of the data
    print('===============================')
    print(f'number of legs = {trip + 1}, total time elapsed = {totalTime:.2f} hr')
        
if __name__ == '__main__':
    main()
