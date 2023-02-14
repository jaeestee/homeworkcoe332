# Homework 3 - Analyzing the Turbidity of Water and Testing it
This homework contains the scripts ``analyze_water.py`` and ``test_analyze_water.py``. The first analyzes the turbidity of water, while the second is a unit tester for the functions in ``analyze_water.py``.

***analyze_water.py***
- This script calculates the turbidity of the most recent five data points by multiplying the calibration constant and the detector current from the data. It also calculates the minimum decay time needed for the turbidity to fall below the safe turbidity threshold.

# Accessing the ``turbidity_data.json`` file
> This json file is pulled straight from user **wjallen**'s ``turbidity`` repository located in ``main``.
Firstly, make sure to import the 
https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
