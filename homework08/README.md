# Navigation:
- [The Data in the Genes + Kubernetes](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#the-data-in-the-genes--kubernetes--images)
- [Image Handling](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#image-handling)
  - [Pulling the Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#pulling-the-image-jaeesteegene_apihw8-from-docker-hub)
  - [Running the Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#running-the-image)
  - [Building a New Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#building-a-new-image)
- [Kubernetes Cluster](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#kubernetes-cluster)
  - [Setting Up the Cluster](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#setting-up-the-cluster)
  - [Testing the Cluster](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#setting-up-the-cluster)
  - [Creating Your Own Image for K8](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#creating-your-own-image-for-k8)
  - [Pushing the New Image for K8](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#pushing-the-new-image-for-k8)
  - [Editing a File for K8](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#editing-a-file-for-k8)
- [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
  - [Load the Data](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-load-the-data-run-this-command)
  - [Delete the Data](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-delete-the-data-run-this-command)
  - [Print the Entire Data](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-the-entire-data-set-whether-it-exists-or-not-run-this-command)
  - [Print List of Gene IDs](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-out-a-list-of-all-gene-ids-in-the-data-set-run-this-command)
  - [Print a Specific Gene](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-specific-data-on-a-gene-run-this-command)
  - [Post the Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-post-the-image-run-this-command)
  - [Delete the Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-delete-the-image-run-this-command)
  - [Get the Image](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-get-the-image-run-this-command)
- [Describing the Gene Data](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#describing-the-gene-data)
  
# The Data in the Genes + Kubernetes + Images
This homework contains the script ``gene_api.py``. This script is a flask and redis application that is used to return data from the Human Genome Organization (HUGO). It also includes sections on how to run the application through the Kubernetes Cluster (K8). The data returned is explained in the sections below.

***```gene_api.py```***
- This flask app contains functions that are called when queries are sent to the running app, therefore returning values that were requested. The functions are:
  - ``delete_data()``, ``post_data()``, ``data()``, ``gene_ids()``, and ``specific_gene_data()``.
> The functions correspond to the queries in the "Queries To Use" section, respectively.

***```deployment-python-debug.yml```***
- This yml file is used for the Kubernetes Cluster and is used to test the program by entering its ```/bin/bash``` interactive terminal.

***```jo25672-test-geneapi-deployment.yml```*** ***```jo25672-test-geneapi-service.yml```***
- These yml files are used for the Kubernetes Cluster and is used to run the gene_api.

***```jo25672-test-redis-deployment.yml```***
***```jo25672-test-redis-pvc.yml```***
***```jo25672-test-redis-service.yml```***
- These yml files are used for the Kubernetes Cluster and is used to run the redis portion of the cluster.
> This helps save the data of the api indefinitely, even if the pods are destroyed.


# Image Handling
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
## Pulling the image ```jaeestee/gene_api:hw8``` from Docker Hub:
To pull the existing image, run this command:
```bash
$ docker pull jaeestee/gene_api:hw8
```
If done properly, ``jaeestee/gene_api:hw8`` should show up with the tag ``hw8`` when running this command:
```bash
$ docker images
```
> The output should look similar to this:
> ```
> REPOSITORY             TAG       IMAGE ID       CREATED         SIZE
> jaeestee/gene_api      hw8       d8376d24fa21   1 hours ago     887MB
> ```


## Running the image:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
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


## Building a New Image:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
To build a new image from the **Dockerfile** present in this directory, run this command:
```
$ docker build -t <dockerhubusername>/gene_api:<version> .
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


# Kubernetes Cluster:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
## Setting Up The Cluster:
To set up the cluster, first run these commands:
```bash
$ kubectl apply -f jo25672-test-geneapi-deployment.yml
$ kubectl apply -f jo25672-test-geneapi-service.yml
$ kubectl apply -f jo25672-test-redis-deployment.yml
$ kubectl apply -f jo25672-test-redis-pvc.yml
$ kubectl apply -f jo25672-test-redis-service.yml
$ kubectl apply -f deployment-python-debug.yml
```
> The deployment-python-debug.yml will be used to test whether the cluster is functioning correctly

Next, use this command to make sure everything is now running properly:
```bash
$ kubectl get pods
```

The output should look similar to this:
```
NAME                                    READY   STATUS    RESTARTS   AGE
jo25672-test-geneapi-67b8c5b8d4-hcg8s   1/1     Running   0          18m
jo25672-test-geneapi-67b8c5b8d4-w5f2w   1/1     Running   0          17m
jo25672-test-redis-5678f8fd88-6njvq     1/1     Running   0          16m
py-debug-deployment-f484b4b99-tprrp     1/1     Running   0          17m
```
> IMPORTANT: Make sure that the status all say Running, else something failed. If it seems to be building, give it some time and try the command again.

Now everything is set up!


## Testing the Kubernetes Cluster:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
To test the cluster and make sure the flask api is functioning properly, use this command to enter the python pod:
```bash
$ kubectl exec -it <py-debug-deployment pod name> -- /bin/bash
```
> IMPORTANT: Make sure to copy and paste the pod name from the pods list that you got earlier.
> Example:
> ```bash
> $ kubectl exec -it py-debug-deployment-f484b4b99-tprrp -- /bin/bash
> ```

If done properly, the command line should change to something like this:
```bash
root@py-debug-deployment-f484b4b99-tprrp:/#
```

Now you can curl using the queries below in the **Queries To Use** section. Just make sure to have the ```localhost``` swapped with ```jo25672-test-geneapi-service```.
For example:
```bash
root@py-debug-deployment-f484b4b99-tprrp:/# curl jo25672-test-geneapi-service:5000/genes
```


## Creating Your Own Image for K8:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
To build a new image from the **Dockerfile** present in this directory, run this command:
```
$ docker build -t <dockerhubusername>/gene_api:hw8 .
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
Successfully tagged jaeestee/gene_api:hw8
```
Now you have successfully created your own image!


## Pushing the New Image for K8:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
Now that your own image was created, it must be pushed for the Kubernetes Cluster to function properly. To do so, use this command:
```bash
$ docker push <dockerhubusername>/gene_api:hw8
```

If done properly, the output should look similar to this:
```
The push refers to repository [docker.io/jaeestee/gene_api]
b7441079a5eb: Layer already exists
739f6e8204e4: Layer already exists
e91a4bead186: Layer already exists
43b09f4e921f: Layer already exists
6ab97ebc930b: Layer already exists
e726038699f2: Layer already exists
b8e0cb862793: Layer already exists
4b4c002ee6ca: Layer already exists
cdc9dae211b4: Layer already exists
7095af798ace: Layer already exists
fe6a4fdbedc0: Layer already exists
e4d0e810d54a: Layer already exists
4e006334a6fd: Layer already exists
hw8: digest: sha256:a722680b5e6dff7fac131dc8128bc1563700e88c67d7c617745ed227b2f066a1 size: 3057
```


## Editing a File for K8:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
Since you have your own image now, you need to edit the ```jo25672-test-geneapi-deployment.yml``` file. To do this, enter into any text editing command like this:
```bash
$ emacs jo25672-test-geneapi-deployment.yml
```

If done properly, the window should look like this:
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jo25672-test-geneapi
  labels:
    app: jo25672-test-geneapi
    username: jo25672
    env: test
spec:
  replicas: 2
  selector:
    matchLabels:
      app: jo25672-test-geneapi
  template:
    metadata:
      labels:
        app: jo25672-test-geneapi
        username: jo25672
        env: test
    spec:
      containers:
        - name: jo25672-test-geneapi
          imagePullPolicy: Always
          image: jaeestee/gene_api:hw8
          env:
          - name: FLASK_APP
            value: "gene_api.py"
          - name: REDIS_IP
            value: jo25672-test-redis-service
          ports:
          - name: http
            containerPort: 5000
```

Now, go all the way to the bottom where it says "image: jaeestee/gene_api:hw8" and make sure that the ```jaeestee``` is switched with your own dockerhub username.
To save the file in ```emacs```, press ```Ctrl+X``` and then ```Ctrl+C```, where it will prompt you to save. Simply press ```y``` on the keyboard.

You have now completed making your own image for the K8 cluster!


# Queries To Use:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)

|Route|Method|What it should do|Easy Navigation|
|---|---|---|---|
|``/data``|POST|Loads in the data|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-load-the-data-run-this-command)|
|``/data``|DELETE|Deletes the data|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-delete-the-data-run-this-command)|
|``/data``|GET|Prints the data|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-the-entire-data-set-whether-it-exists-or-not-run-this-command)|
|``/genes``|GET|Prints the gene IDs|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-out-a-list-of-all-gene-ids-in-the-data-set-run-this-command)|
|``/genes/<hgnc_id>``|GET|Prints a specific gene|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-print-specific-data-on-a-gene-run-this-command)|
|``/image``|POST|Posts the image|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-post-the-image-run-this-command)|
|``/image``|DELETE|Deletes the image|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-delete-the-image-run-this-command)|
|``/image``|GET|Gets the image|[Click Me](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#to-get-the-image-run-this-command)|

## To load the data, run this command:
```bash
$ curl localhost:5000/data -X POST
```
If done properly, the output should look like this:
```
Successfully reloaded the dictionary with the data from the web!
```


## To delete the data, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
```bash
$ curl localhost:5000/data -X DELETE
```
If done properly, the output should look like this:
```
Successfully deleted all the data from the dictionary!
```


## To print the entire data set (whether it exists or not), run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
```bash
$ curl localhost:5000/data
```
> This will send a get request using curl to the app that should be running.

If done properly, the end of the output should look similar to one of these 2 output possibilities:
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


## To print out a list of all gene IDs in the data set, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
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


## To print specific data on a gene, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
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


## To post the image, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
```bash
$ curl localhost:5000/image -X POST
```

If done properly, the output should be this:
```
Successfully posted the image!
```

If there wasn't any data, the output should be this:
```
The data does not exist...
```


## To delete the image, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
```bash
$ curl localhost:5000/image -X DELETE
```

If done properly, the output should be this:
```
Successfully deleted all the data from the dictionary!
```


## To get the image, run this command:
> Back to [Queries to Use](https://github.com/jaeestee/homeworkcoe332/tree/main/homework08#queries-to-use)
```bash
$ curl --output image.png localhost:5000/image
```
> the new ``--output image.png`` means that the output will be stored into ``image.png`` in the current directory

If done properly, the output should look similar to this:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 25908  100 25908    0     0  3614k      0 --:--:-- --:--:-- --:--:-- 3614k
```

To check whether the image actually successfully went through, run the command without the ``--output image.png``:
```bash
$ curl localhost:5000/image
```

If it worked, the output should look similar to this:
```
Warning: Binary output can mess up your terminal. Use "--output -" to tell
Warning: curl to output it to your terminal anyway, or consider "--output
Warning: <FILE>" to save to a file.
```
> This is why the ``--output image.png`` needs to be added to successfully download the image.

If there isn't any data, this will be the output:
```
The data does not exist...
```


# Describing the Gene Data:
> Back up to [Navigation](https://github.com/jaeestee/homeworkcoe332/blob/main/homework08/README.md#navigation)
This gene data was provided by the HUGO Gene Nomenclature Committee. This committee is a part of the Human Genome Organization (HUGO) and oversees the approval of every gene name. Therefore, HGNC assigns every gene an HGNC ID, a gene symbol, an approved name, and many more (for more details, check out the website below).
> From the [HGNC Complete Set Archive](https://www.genenames.org/download/archive/)

In this application, the data was pulled from this specific url, [Current JSON format hgnc_complete_set file](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json), which is located at the very bottom of their website.
