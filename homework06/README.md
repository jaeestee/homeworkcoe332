# Navigation:
- put stuff here
  
# The Data in the Genes
This homework contains the script ``gene_api.py``. This script is a flask application that is used to return data from the Human Genome Organization (HUGO). The data returned is explained in the sections below.

***gene_api.py***
- This flask app contains functions that are called when queries are sent to the running app, therefore returning values that were requested. The functions are:
  - ``delete_data()``, ``post_data()``, ``data()``, ``gene_ids()``, and ``specific_gene_data()``.
> The functions correspond to the queries in the "Queries To Use" section, respectively.

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
# Image Handling
## Pulling the image ```jaeestee/gene_api``` from Docker Hub:
To pull the existing image, run this command:
```bash
$ docker pull jaeestee/gene_api
```
If done properly, ``jaeestee/gene_api`` should show up with the tag ``latest`` when running this command:
```bash
$ docker images
```
> The output should look similar to this:
> ```
> REPOSITORY             TAG       IMAGE ID       CREATED         SIZE
> jaeestee/gene_api      latest    d8376d24fa21   1 hours ago     887MB
> ```

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## Running the image:
To start running the containerized Flask app, run this command:
```bash
docker-compose up
```
> Remember that the docker-compose.yml file must exist in the same folder for this to work!
If done properly, the output should look similar to this:
```
Successfully built 35ead5be0a90
Successfully tagged jaeestee/gene_api:latest
WARNING: Image for service flask-app was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating homework06_flask-app_1 ... done
Attaching to homework06_flask-app_1
flask-app_1  |  * Serving Flask app 'gene_api'
flask-app_1  |  * Debug mode: on
flask-app_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
flask-app_1  |  * Running on all addresses (0.0.0.0)
flask-app_1  |  * Running on http://127.0.0.1:5000
flask-app_1  |  * Running on http://172.20.0.2:5000
flask-app_1  | Press CTRL+C to quit
flask-app_1  |  * Restarting with stat
flask-app_1  |  * Debugger is active!
flask-app_1  |  * Debugger PIN: 436-748-674
```
Now the app is running!
> **IMPORTANT: Have this running on a separate window and keep it running while sending queries!!!**

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## Building a New Image:
To build a new image from the **Dockerfile** present in this directory, run this command:
```
$ docker build -t <dockerhubusername>/iss_tracker:<version> .
```
> **IMPORTANT: Make sure to be in the same directory as the ``Dockerfile`` and DO NOT FORGET THE "." at the very end of this command!!!**

If done properly, the output should look similar to this:
```
Sending build context to Docker daemon   21.5kB
Step 1/5 : FROM python:3.8.10
 ---> a369814a9797
Step 2/5 : RUN pip install Flask==2.2.2
 ---> Using cache
 ---> bbf69ba6f74f
Step 3/5 : RUN pip install requests==2.22.0
 ---> Using cache
 ---> 4ffa49d19ef5
Step 4/5 : COPY gene_api.py /gene_api.py
 ---> 2bcad41d3385
Step 5/5 : CMD ["python", "gene_api.py"]
 ---> Running in c12334c932b1
Removing intermediate container c12334c932b1
 ---> 573a6ad42ef6
Successfully built 573a6ad42ef6
Successfully tagged jaeestee/gene_api:latest
```
Now you have successfully created your own image!

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
# Queries To Use (**WITH THE APP RUNNING ON A SEPARATE TAB**):
## To load/reload the data, run this command:
```bash
$ curl localhost:5000/data -X POST
```
If done properly, the output should look like this:
```
Successfully reloaded the dictionary with the data from the web!
```

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## To delete the data, run this command:
```bash
$ curl localhost:5000/data -X DELETE
```
If done properly, the output should look like this:
```
Successfully deleted all the data from the dictionary!
```

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## To print the entire data set (whether it exists or is empty), run this command:
```bash
$ curl localhost:5000/data
```
> This will send a get request using curl to the app that should be running.

If done properly, the end of the output should look similar to one of these 3 outputs:
- Output possibility 1:
```
    ],
    "numFound": 43625,
    "start": 0
  },
  "responseHeader": {
    "QTime": 26,
    "status": 0
  }
}
```
> This will print out the entire data set, but as long as you see something similar to this last section, it printed everything properly.

- Output possibility 2:
```
The data set does not exist yet!
```
> This means that the POST method has not been called.

- Output possibility 3:
```
{}
```
> This means that the DELETE method was called, emptying the data.

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## To print out a list of all gene IDs in the data set, run this command:
```bash
$ curl localhost:5000/genes
```
If done properly, the end of the output should look similar to this:
```
  "HGNC:25468",
  "HGNC:13195",
  "HGNC:13198",
  "HGNC:13199",
  "HGNC:28160",
  "HGNC:32058",
  "HGNC:38032",
  "HGNC:25820",
  "HGNC:13200",
  "HGNC:51695",
  "HGNC:29027",
  "HGNC:24523"
]
```
> An error message will appear if the data is empty or doesn't exist yet. Additionally, there should be a lot more data points, this is just a shortened version.

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
## To print specific data on a gene, run this command:
```bash
$ curl localhost:5000/genes/<geneID>
```
> Make sure to replace the geneID with a specific gene ID as shown below:
> ```bash
> $ curl localhost:5000/genes/HGNC:24523
> ```
If done properly, the output should look similar to this:
```
  "hgnc_id": "HGNC:24523",
  "location": "1p31.1",
  "location_sortable": "01p31.1",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000370801.8",
    "NM_015534.6"
  ],
  "mgd_id": [
    "MGI:1920453"
  ],
  "name": "zinc finger ZZ-type containing 3",
  "omim_id": [
    "619892"
  ],
  "pubmed_id": [
    16428443,
    21304275
  ],
  "refseq_accession": [
    "NM_015534"
  ],
  "rgd_id": [
    "RGD:1565468"
  ],
  "status": "Approved",
  "symbol": "ZZZ3",
  "ucsc_id": "uc001dhq.4",
  "uniprot_ids": [
    "Q8IYH5"
  ],
  "uuid": "4d059d1d-7f62-4038-ae78-9f451f5a5c5a",
  "vega_id": "OTTHUMG00000009652"
}
```
> A message will appear if the data is empty or doesn't exist yet. Note: This is a shortened version of the data that should be printed.

# Describing the Gene Data:
This gene data was provided by the HUGO Gene Nomenclature Committee. This committee is a part of the Human Genome Organization (HUGO) and oversees the approval of every gene name. Therefore, HGNC assigns every gene an HGNC ID, a gene symbol, an approved name, and many more (for more details, check out the website below).
> From the [HGNC Complete Set Archive](https://www.genenames.org/download/archive/)

In this application, the data was pulled from this specific url, [Current JSON format hgnc_complete_set file](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json), which is located at the very bottom of their website.

> Back up to [Navigation](https://github.com/jaeestee/ISS-Tracker/blob/main/README.md#navigation)
