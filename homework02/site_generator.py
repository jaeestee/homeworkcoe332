# site_generator: generates 5 random meteorite landing sites.

#importing the needed libraries
import random
import json

def create_random_coordinates() -> list:
    """
    This function returns a random latitude and longitude. The latitude
    is a float between 16.0 and 18.0 degrees North while the longitude
    is a float between 82.0 and 84.0 degrees East.

    Returns:
        result (list): A list of floats containing the latitude and longitude.
    """

    #creates a random latitude and longitude
    randomLatitude = random.uniform(16.0, 18.0)
    randomLongitude = random.uniform(82.0, 84.0)

    #returns the latitude and longitude
    return [randomLatitude, randomLongitude]
    
def pick_random_composition() -> str:
    """
    This function returns a random composition from the given list.
    The given list contains "stony", "iron", and "stony-iron".

    Returns:
        result (string): A random composition from the list.
    """

    #the given list of compositions
    listOfCompositions = ["stony", "iron", "stony-iron"]

    #chooses randomly from the list
    randomComposition = random.choice(listOfCompositions)

    #returns the corresponding value
    return(randomComposition)

def main():
    """
    This main function compiles all the needed data and puts it
    into a dictionary to then later save it into a JSON file.
    The needed data contains the site_id, latitude, longitude,
    and composition.
    """

    #the dictionary to store all the data
    siteDictionary = {'sites' :[]}

    #for-loop to add the random meteorite landing sites
    for id in range(1, 6):
        siteDictionary['sites'].append({'site_id': id, 'latitude': create_random_coordinates()[0], 'longitude': create_random_coordinates()[1], 'composition': pick_random_composition()})
        
    #assembles all the information into a json file
    with open('random_meteorites.json', 'w') as out:
        json.dump(siteDictionary, out, indent=2)
        

if __name__ == '__main__':
    main()
