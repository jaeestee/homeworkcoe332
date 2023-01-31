# Homework 2
> This homework contains a script ``site_generator.py`` and ``trip_calculator.py``. Using these scripts, it creates 5 random meteorites sites and calculates a trip a robot would take while moving along the sites.

site_generator
- This script generates five random meteorite landing sites and saves the data into a JSON file called ``random_meteorites.json``. This contains a random latitude between 16.0 and 18.0 degrees North and a random longitude between 82.0 and 84.0 degrees East. It also contains a random composition from the list (stony, iron, stony-iron) and contains a site id. Then all five meteorite landing sites are assembled into a dictionary with the "sites" key.

trip_calculator
- This script uses the generated file, ``random_meteorites.json``, to calculate a total travel time from site to site and a sample time for each composition of meteorite. The speed of the robot is **10 km/hr** and the robot starts at the latitude of **16.0** and the longitude of/ **82.0**. We are to assume that the radius of Mars is **3389.5 km**.
