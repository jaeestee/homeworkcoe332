# Navigation:
- [Homework 5 (Description)](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#homework-5---Containing-the-Advanced-ISS-Trajectory)
- [Queries To Use While The App is Running:](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#queries-to-use-while-the-app-is-running)
  - [To print the entire data set](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#to-print-the-entire-data-set-run-this-command)
  - [To print out a list of all Epochs in the data set](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#to-print-out-a-list-of-all-epochs-in-the-data-set-run-this-command)
  - [To print a specific Epoch](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#to-print-a-specific-epoch-run-this-command)
  - [To print the speed of a specific Epoch](https://github.com/jaeestee/homeworkcoe332/tree/main/homework05#to-print-the-speed-of-a-specific-epoch-run-this-command)
# Homework 5 - Containing the Advanced ISS Trajectory
This homework contains the script ``iss_tracker.py``. This script is a flask application that is used to return data from the iss trajectory data. The data returned is explained in the sections below.

***iss_tracker.py***
- This flask app contains functions that are called when queries are sent to the running app, therefore returning values that were requested. The functions are ``data()``, ``epoch_data()``, ``specific_epoch_data()``, and ``calculate_epoch_speed()``.
> The functions correspond to the queries down below, respectively.

# Pulling the image ```jaeestee/iss_tracker``` from Docker Hub:
To pull the existing image, run this command:
```bash
$ docker pull jaeestee/iss_tracker:hw05
```
If done properly, ``jaeestee/iss_tracker`` should show up with the tag ``hw05`` when running this command:
```bash
$ docker images
```
> The output should look similar to this:
> ```
> REPOSITORY             TAG       IMAGE ID       CREATED         SIZE
> jaeestee/iss_tracker   hw05      d8276d24fa21   2 hours ago     897MB
> ```

# Running the image:
To start running the containerized Flask app, run this command:
```bash
docker run -it --rm -p 5000:5000 jaeestee/iss_tracker:hw05
```
If done properly, the output should look similar to this:
```
 * Serving Flask app 'iss_tracker'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 953-963-822
```
Now the app is running!
> **IMPORTANT: Have this running on a separate window and keep it running while sending queries!!!**

# Queries To Use While The App is Running:
## To print the entire data set, run this command:
```bash
$ curl localhost:5000/
```
> This will send a get request using curl to the app that should be running.
If done properly (**WITH THE APP RUNNING**), the end of the output should look similar to this:
```
"metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-048T12:00:00.000Z",
            "STOP_TIME": "2023-063T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-049T01:38:49.191Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```
> This will print out the entire data set, but as long as you see the metadata section, it printed everything properly.

## To print out a list of all Epochs in the data set, run this command:
```bash
$ curl localhost:5000/epochs
```
If done properly, the end of the output should look similar to this:
```
"EPOCH": "2023-063T12:00:00.000Z",
    "X": {
      "#text": "2820.04422055639",
      "@units": "km"
    },
    "X_DOT": {
      "#text": "5.0375825820999403",
      "@units": "km/s"
    },
    "Y": {
      "#text": "-5957.89709645725",
      "@units": "km"
    },
    "Y_DOT": {
      "#text": "0.78494316057540003",
      "@units": "km/s"
    },
    "Z": {
      "#text": "1652.0698653803699",
      "@units": "km"
    },
    "Z_DOT": {
      "#text": "-5.7191913150960803",
      "@units": "km/s"
    }
  }
]
```

## To print a specific Epoch, run this command:
```bash
$ curl localhost:5000/epochs/epochKey
```
> Make sure to replace the epochKey with a specific Epoch as shown below:
> ```bash
> $ curl localhost:5000/epochs/2023-063T12:00:00.000Z
> ```
If done properly, the output should look similar to this:
```
{
  "EPOCH": "2023-063T12:00:00.000Z",
  "X": {
    "#text": "2820.04422055639",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "5.0375825820999403",
    "@units": "km/s"
  },
  "Y": {
    "#text": "-5957.89709645725",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "0.78494316057540003",
    "@units": "km/s"
  },
  "Z": {
    "#text": "1652.0698653803699",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "-5.7191913150960803",
    "@units": "km/s"
  }
}
```

## To print the speed of a specific Epoch, run this command:
```bash
$ curl localhost:5000/epochs/2023-063T12:00:00.000Z/speed
```
If done properly, the output should look similar to this:
```
Speed: 7.661757196327827 km/s
```
