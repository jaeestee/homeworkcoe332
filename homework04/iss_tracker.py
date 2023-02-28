from flask import Flask
import requests, xmltodict, math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def data() -> dict:
    """
    This function imports the data into the data variable directly from the website so that it can always
    use the most updated data set. Then it returns the said data in the form of a dictionary.

    Returns:
        data (dict): The entire iss data.
    """

    #stores the data from the get request into the data variable and converts it into a dictionary
    data = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(data.text)

    return data

@app.route('/epochs', methods=['GET'])
def epoch_data() -> list:
    """
    This function calls the get_data() function to retrieve the entire data set and returns the listOfEpochs
    variable.

    Returns:
        listOfEpochs (list): The entire list of Epochs from the iss data.
    """

    #stores the entire epoch data by navigating through the entire data dictionary
    listOfEpochs = data()['ndm']['oem']['body']['segment']['data']['stateVector']

    return listOfEpochs

@app.route('/epochs/<string:epoch>', methods=['GET'])
def specific_epoch_data(epoch: str) -> dict:
    """
    This function returns the specific epoch data that was requested by the user.

    Args:
        epoch (str): The specific epoch key to find the requested epoch data.

    Returns:
        epochData (dict): The epoch data for the given epoch key.
    """

    #stores the list of epochs using the pre-existing function
    listOfEpochs = epoch_data()

    #shorts through the list to match the epoch key and returns the data for it
    for i in range(len(listOfEpochs)):
        if listOfEpochs[i]['EPOCH'] == epoch:
            return listOfEpochs[i]

    #if it doesn't find it, returns this prompt
    return 'Could not find the epoch for the given key.\n'

@app.route('/epochs/<string:epoch>/speed', methods=['GET'])
def calculate_epoch_speed(epoch: str) -> dict:
    """
    This function calculates the speed for the specific epoch and returns it.

    Args:
        epoch (str): The specific epoch key to find the requested epoch data.

    Returns:
        speed (float): The speed for the specific epoch requested.
    """

    #stores the specific epoch using the pre-existing function
    specificEpoch = specific_epoch_data(epoch)

    #stores the X_DOT, Y_DOT, and Z_DOT for the specific epoch into corresponding variables and converts them to float
    xDot = float(specificEpoch['X_DOT']['#text'])
    yDot = float(specificEpoch['Y_DOT']['#text'])
    zDot = float(specificEpoch['Z_DOT']['#text'])

    #the units for the vector
    units = specificEpoch['X_DOT']['@units']
    
    #calculates the speed using the magnitude of a vector formula
    speed = math.sqrt(xDot**2 + yDot**2 + zDot**2)

    return f'Speed: {str(speed)} {units}\n'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
