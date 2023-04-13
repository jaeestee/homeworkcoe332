from flask import Flask, request
import requests, redis, json
import os
import matplotlib.pyplot as plt

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()

app = Flask(__name__)

rd = redis.Redis(host=redis_ip, port=6379, db=0, decode_responses=True)

@app.route('/data', methods=['DELETE'])
def delete_data() -> str:
    """
    This function deletes the data completely.

    Returns:
        message (str): Message saying that the data was deleted.
    """
    
    #deletes the entire data set from the redis client
    rd.flushdb()

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
    
    #stores the data from the get request into the data variable and converts it into a dictionary
    data = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    data = data.json()

    #stores the data into the redis client, but as a serialized dictionary string
    rd.set('data', json.dumps(data))

    #the success message
    message = 'Successfully reloaded the dictionary with the data from the web!\n'
    
    return message
    
@app.route('/data', methods=['GET'])
def data() -> dict:
    """
    This function returns the data from Redis, but only if it exists or is empty.
    Otherwise it will return a message saying that the data does not exist.

    Returns:
        redisData (dict): The entire gene data.
    """

    #try-except block that returns if the data doesn't exist and an error occurs because of it
    try:
        #un-seralizing the string into a dictionary
        redisData = json.loads(rd.get('data'))
    except NameError:
        return 'The data does not exist...\n'
    except TypeError:
        return 'The data does not exist...\n'
    
    return redisData

@app.route('/genes', methods=['GET'])
def gene_ids() -> list:
    """
    This function tries to retrieve the data from the data() function and will print the list of
    gene IDs if the data set exists. If it is empty or doesn't exist, it will print out an error
    message.

    Returns:
        results (list): The entire list of gene IDs.
    """

    #try-except block that makes sure it returns a message if the data is empty or doesn't exist
    try:
        #stores the entire gene data by navigating through the entire data dictionary
        listOfGenes = data()['response']['docs']
    except TypeError:
        return 'The data does not exist...\n'
    except KeyError:
        return 'The data does not exist...\n'

    #initializing a new blank list to store the "new" data
    results = []

    #for loop that stores the requested gene ID data
    for i in range(len(listOfGenes)):
        results.append(listOfGenes[i]['hgnc_id'])
    
    return results

@app.route('/genes/<string:geneID>', methods=['GET'])
def specific_gene_data(geneID: str) -> dict:
    """
    This function returns the specific gene data that was requested by the user.
    However, if the data set is empty or doesn't exist, it will return an error
    message.

    Args:
        geneID (str): The specific gene ID to find the requested gene data.

    Returns:
        genesDict (dict): The gene data for the given gene ID.
    """
    
    #try-except block to make sure the data has information
    try:
        genesDict = data()['response']['docs']
    except TypeError:
        return 'The data does not exist...\n'
    except NameError:
        return 'The data does not exist...\n'
    except KeyError:
        return 'The data does not exist...\n'
    
    #sorts through the list to match the gene ID and returns the data for it
    for i in range(len(genesDict)):
        if genesDict[i]['hgnc_id'] == geneID:
            return genesDict[i]

    #if it doesn't find it, returns this prompt
    return 'Could not find the gene data for the given ID.\n'

rdi = redis.Redis(host=redis_ip, port=6379, db=1, decode_responses=True)

@app.route('/image', methods=['POST'])
def post_image():
    """
    This function creates the image using the data, if present, and stores it into the rdi client.

    Returns:
        message (str): Message saying that the image was successfully posted.
    """

    #try-except block to make sure the data has information
    try:
        genesDict = data()['response']['docs']
    except TypeError:
        return 'The data does not exist...\n'
    except NameError:
        return 'The data does not exist...\n'
    except KeyError:
        return 'The data does not exist...\n'

    #initializing the x-axis data points
    x = []
    
    #sorts through the list to match the gene ID and returns the data for it
    for i in range(len(genesDict)):
        hgnc = genesDict[i]['hgnc_id']
        x.append((int)hgnc[5:])
    
    #stores the image into the rdi client
    rdi.set('image', x)

    #the success message
    message = 'Successfully posted the image!\n'

    return x
    
@app.route('/image', methods=['DELETE'])
def delete_image():
    """
    This function removes the image from the database.

    Returns:
        message (str): Message saying that the data was deleted.
    """

    #deletes all data from the rdi client
    rdi.flushdb()

    message = 'Successfully deleted the image!\n'
    return message
    
@app.route('/image', methods=['GET'])
def get_image():
    """
    This function returns the image, if it exists, from the rdi client.

    Returns:
    
    """
    try:
        rdi.get('image')
    except NameError:
        return 'The data does not exist...\n'
    except TypeError:
        return 'The data does not exist...\n'
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
