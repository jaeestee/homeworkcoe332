import requests

#the turbidity threshold and decay factor constants
TURBIDITY_THRESHOLD = 1.0
DECAY_FACTOR = 0.02

def calculate_turbidity(data: list, calibrationKey: str, detectorKey: str) -> float:
    """
    This function calcuates and returns the turbidity of the most recent five data points using
    the calibration constant and the detector current from the data.

    Args:
        data (list): The list containing the turbidity data.
        calibrationKey (str): The calibration constant key to retrieve the calibration constant.
        detectorCurrent (str): The dectector current key to retrieve the ninety degree detector current.

    Returns:
        turbidity (float): The average turbidity of the most recent five data points.
    """

    #initializing the turbidityTotal variable
    turbidityTotal = 0

    #for-loop to calculate the total turbidity of the most recent five data points
    for i in range(5):
        calibrationConstant = data[i][calibrationKey]
        detectorCurrent = data[i][detectorKey]
        turbidityTotal = turbidityTotal + calibrationConstant * detectorCurrent

    #calculates the average
    turbidity = turbidityTotal / 5

    #returns the turbidity average
    return turbidity

def calculate_decay_time(turbidity: float) -> float:
    """
    This function calculates and returns the minimum time for the turbidity to fall below the safe water
    threshold.

    Args:
        turbidity (float): The turbidity of the most recent five data points. This is calculated in the
        calculate_turbidity function.

    Returns:
        hoursElapsed (float): The minimum hours elapsed for the turbidity to fall below a safe threshold.
    """

    #initializing the hoursElapsed and accuracy variables
    hoursElapsed = 0
    accuracy = 0.01

    #while loop to calculate the minimum hours elapsed
    while TURBIDITY_THRESHOLD < (turbidity * (1 - DECAY_FACTOR)**(hoursElapsed + accuracy)):
        hoursElapsed = hoursElapsed + accuracy

    #returns the hours elapsed
    return hoursElapsed

def main():
    #requesting the data from an http address 
    data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')

    #convert the data that are in bytes into json and store it as a dictionary back into the data variable
    data = data.json()

    #calls the calculate_turbidity function to get the turbidity
    turbidity = calculate_turbidity(data['turbidity_data'], 'calibration_constant', 'detector_current')

    #prints the turbidity message
    print(f'Average turbidity based on most recent five measurements = {turbidity:.4f} NTU')

    #prints whether the turbidity is above or below the safe threshold
    if turbidity > TURBIDITY_THRESHOLD:
        print('Warning: Turbidity is above threshold for safe use')
    else:
        print('Info: Turbidity is below treshold for safe use')

    #calls the calculate_decay_time function to get the hours elapsed
    hoursElapsed = calculate_decay_time(turbidity)

    #prints the minimum time required message
    print(f'Minimum time required to return below a safe threshold = {hoursElapsed:.2f} hours')
        
    
if __name__ == '__main__':
    main()
