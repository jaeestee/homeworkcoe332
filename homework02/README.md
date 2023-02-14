# Homework 2 - Trip Generator for Random Meteorite Landing Sites
This homework contains the scripts ``site_generator.py`` and ``trip_calculator.py``. Using these scripts, it creates **5** random meteorites sites and calculates a trip a robot would take while moving along the randomly generated sites.

***site_generator.py***
- This script generates five random meteorite landing sites that contain a site id, latitude, longitude, and composition of the meteorite. Then it assembles the data into a dictionary and writes it into a JSON file called ``random_meteorites.json``.
> This contains a random latitude (between 16.0 and 18.0 degrees North) and a random longitude (between 82.0 and 84.0 degrees East). It also contains a random composition from the list (stony, iron, stony-iron) and contains a site id. Then all five meteorite landing sites are assembled into a dictionary with the "sites" key.

***trip_calculator.py***
- This script uses the generated file, ``random_meteorites.json``, to calculate a total travel time from site to site (using the great-circle distance algorithm) and a sample time for each composition of meteorite. Then it prints out how many legs there are in the trip and the total time elapsed during this trek.
> The speed of the robot is **10 km/hr** and the robot starts at the latitude of **16.0** and the longitude of **82.0**. We are to assume that the radius of Mars is **3389.5 km**.

## Running the Code
This homework requires the ``site_generator.py`` to create the json file with **5** random sites and then calculating the trip with ``trip_calculator.py``.

Firstly, run ``site_generator.py``:
```bash
$ python3 site_generator.py
```
> Using the ``ls`` command in the terminal, it will show the newly created file called ``random_meteorites.json``.

Next, run ``trip_calculator.py``:
```bash
$ python3 trip_calculator.py
```

If done properly, the output should look like this (but with different numbers):
```
leg = 1, time to travel = 13.15 hr, time to sample = 3 hr
leg = 2, time to travel = 6.09 hr, time to sample = 3 hr
leg = 3, time to travel = 1.55 hr, time to sample = 3 hr
leg = 4, time to travel = 4.08 hr, time to sample = 1 hr
leg = 5, time to travel = 6.26 hr, time to sample = 2 hr
===============================
number of legs = 5, total time elapsed = 43.13 hr
```
> These results show the travel time between each site, in order, and the time it takes to sample the specific meteorite. Lastly, they show the total number of legs there are in the trip and the total time elapsed (summing the traveling time and the sampling time).
