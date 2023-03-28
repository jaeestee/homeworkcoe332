from flask import Flask, request
import requests, math

app = Flask(__name__)

@app.route('/data', methods=['DELETE'])
def delete_data() -> str:
    """
    This function deletes the data and replaces the data with a blank dictionary.

    Returns:
        message (str): Message saying that the data was deleted.
    """

    #making DATA a global variable
    global DATA

    #simply setting DATA equal to nothing so that it "deletes" the data
    DATA = {}

    message = 'Successfully deleted all the data from the dictionary!\n'
    return message

@app.route('/data', methods=['POST'])
def post_data() -> str:
    """
    This function adds the DATA dictionary object with the data from the web and returns
    a success message.

    Returns:
        message (str): Message saying that the data was successfully reloaded.
    """

    #making DATA a global variable
    global DATA
    
    #stores the data from the get request into the data variable and converts it into a dictionary
    DATA = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    DATA = DATA.json()

    message = 'Successfully reloaded the dictionary with the data from the web!\n'
    return message
    
@app.route('/data', methods=['GET'])
def data() -> dict:
    """
    This function returns the data, but only if it exists or is empty. Otherwise
    it will return a message saying that the data does not exist.

    Returns:
        data (dict): The entire gene data.
    """

    #try-except block that returns if the data doesn't exist and an error occurs because of it
    try:
        DATA
    except NameError:
        return 'The data set does not exist yet!\n'

    return DATA

@app.route('/genes', methods=['GET'])
def gene_ids() -> list:
    """
    This function calls the get_data() function to retrieve the entire data set and returns the listOfEpochs
    variable. It can take in query parameters of offset and limit which will cause the data to start at a
    different point and limit the amount of data returned.

    Returns:
        results (list): The results from the entire list of Epochs from the iss data considering the offset and
        limit parameters.
    """

    #try-except block that makes sure it returns a message if the data is empty or doesn't exist
    try:
        #stores the entire epoch data by navigating through the entire data dictionary
        listOfGenes = data()['response']['docs']
    except TypeError:
        return 'The data set does not exist yet!\n'
    except KeyError:
        return 'The data is empty!\n'

    #initializing a new blank list to store the "new" data
    results = []

    #for loop that stores the requested Epoch data
    for i in range(len(listOfGenes)):
        results.append(listOfGenes[i]['hgnc_id'])
    
    return results

@app.route('/genes/<string:geneID>', methods=['GET'])
def specific_gene_data(geneID: str) -> dict:
    """
    This function returns the specific epoch data that was requested by the user.

    Args:
        epoch (str): The specific epoch key to find the requested epoch data.

    Returns:
        epochData (dict): The epoch data for the given epoch key.
    """
    
    #try-except block to make sure the data has information
    try:
        listOfGenes = data()['response']['docs']
    except TypeError:
        return 'The data seems to be empty or does not exist...\n'
    except NameError:
        return 'The data seems to be empty or does not exist...\n'
    except TypeError:
        return 'The data seems to be empty or does not exist...\n'

    #shorts through the list to match the epoch key and returns the data for it
    for i in range(len(listOfGenes)):
        if listOfGenes[i]['hgnc_id'] == geneID:
            return listOfGenes[i]

    #if it doesn't find it, returns this prompt
    return 'Could not find the epoch for the given key.\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
