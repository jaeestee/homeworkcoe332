# Navigation:
- [The Data in the Genes](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#the-data-in-the-genes)
- [Image Handling](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#image-handling)
  - [Pulling the Image](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#running-the-image)
  - [Running the Image](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#running-the-image)
  - [Building a New Image](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#building-a-new-image)
- [Queries to Use](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#queries-to-use)
  - [Load/Reload the Data](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#to-load-the-data-run-this-command)
  - [Delete the Data](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#to-delete-the-data-run-this-command)
  - [Print the Entire Data](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#to-print-the-entire-data-set-whether-it-exists-or-is-empty-run-this-command)
  - [Print List of Gene IDs](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#to-print-out-a-list-of-all-gene-ids-in-the-data-set-run-this-command)
  - [Print a Specific Gene](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#to-print-specific-data-on-a-gene-run-this-command)
- [Describing the Gene Data](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#describing-the-gene-data)
  
# The Data in the Genes
This homework contains the script ``gene_api.py``. This script is a flask and redis application that is used to return data from the Human Genome Organization (HUGO). The data returned is explained in the sections below.

***gene_api.py***
- This flask app contains functions that are called when queries are sent to the running app, therefore returning values that were requested. The functions are:
  - ``delete_data()``, ``post_data()``, ``data()``, ``gene_ids()``, and ``specific_gene_data()``.
> The functions correspond to the queries in the "Queries To Use" section, respectively.

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
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

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
## Running the image:
To start running the containerized Flask app, run this command:
```bash
$ docker-compose up -d
```
> Remember that the docker-compose.yml file must exist in the same folder for this to work!
If done properly, the output should look similar to this:
```
Creating network "homework06_default" with the default driver
Creating homework06_redis-db_1 ... done
Creating homework06_flask-app_1 ... done
```
Now the app is running!
> **IMPORTANT: This does not have to be running on a separate tab since it is running in the background using the ``-d`` command!!!**

To check that the application is running, run this command:
```bash
$ docker ps
```
If the application is running properly, the output should look similar to this:
```
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS        PORTS                                       NAMES
8a314bf73084   jaeestee/gene_api   "python gene_api.py"     2 seconds ago   Up 1 second   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   homework06_flask-app_1
de1d39e3cab4   redis:7             "docker-entrypoint.s…"   2 seconds ago   Up 1 second   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework06_redis-db_1
```
> If not, the output should look similar to this:
> ```
> CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS        PORTS                                       NAMES
> ```

To stop the application from running in the background, run this command:
```bash
$ docker-compose down
```
If done properly, the output should look similar to this:
```
Stopping homework06_flask-app_1 ... done
Stopping homework06_redis-db_1  ... done
Removing homework06_flask-app_1 ... done
Removing homework06_redis-db_1  ... done
Removing network homework06_default
```

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
## Building a New Image:
To build a new image from the **Dockerfile** present in this directory, run this command:
```
$ docker build -t <dockerhubusername>/iss_tracker:<version> .
```
> **IMPORTANT: Make sure to be in the same directory as the ``Dockerfile`` and DO NOT FORGET THE "." at the very end of this command!!!**

If done properly, the output should look similar to this:
```
Sending build context to Docker daemon  19.46kB
Step 1/6 : FROM python:3.8.10
 ---> a369814a9797
Step 2/6 : RUN pip install Flask==2.2.2
 ---> Using cache
 ---> bbf69ba6f74f
Step 3/6 : RUN pip install requests==2.22.0
 ---> Using cache
 ---> 4ffa49d19ef5
Step 4/6 : RUN pip install redis==4.5.1
 ---> Using cache
 ---> c5c9cd8cc964
Step 5/6 : COPY gene_api.py /gene_api.py
 ---> 06dc8f8ebd53
Step 6/6 : CMD ["python", "gene_api.py"]
 ---> Running in b7b7f007b29f
Removing intermediate container b7b7f007b29f
 ---> 2a2936689823
Successfully built 2a2936689823
Successfully tagged jaeestee/gene_api:latest
```
Now you have successfully created your own image!

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
# Queries To Use:
## To load the data, run this command:
```bash
$ curl localhost:5000/data -X POST
```
If done properly, the output should look like this:
```
Successfully reloaded the dictionary with the data from the web!
```

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
## To delete the data, run this command:
```bash
$ curl localhost:5000/data -X DELETE
```
If done properly, the output should look like this:
```
Successfully deleted all the data from the dictionary!
```

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
## To print the entire data set (whether it exists or not), run this command:
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
The data does not exist...
```
> This means that the POST method has not been called or that the DELETE method was called.

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
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

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
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

> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
# Describing the Gene Data:
This gene data was provided by the HUGO Gene Nomenclature Committee. This committee is a part of the Human Genome Organization (HUGO) and oversees the approval of every gene name. Therefore, HGNC assigns every gene an HGNC ID, a gene symbol, an approved name, and many more (for more details, check out the website below).
> From the [HGNC Complete Set Archive](https://www.genenames.org/download/archive/)

In this application, the data was pulled from this specific url, [Current JSON format hgnc_complete_set file](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json), which is located at the very bottom of their website.
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework06/README.md#navigation)
