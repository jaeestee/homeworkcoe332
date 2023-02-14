# Homework 3 - Analyzing the Turbidity of Water and Testing it
This homework contains the scripts ``analyze_water.py`` and ``test_analyze_water.py``. The first analyzes the turbidity of water, while the second is a unit tester for the functions in ``analyze_water.py``.

***analyze_water.py***
- This script calculates the turbidity of the most recent five data points by multiplying the calibration constant and the detector current from the data. It also calculates the minimum decay time needed for the turbidity to fall below the safe turbidity threshold.
> The ``calculate_turbidity`` function calculates the turbidity while the ``calculate_decay_time`` function calculates the minimum time to fall below the safe threshold.

***test_analyze_water.py***
- This script contains unit tests to test the ``analyze_water.py`` functions ``calculate_turbidity`` and ``calculate_decay_time`` using pytest.

# Running the Code
This homework relies solely on the ``analyze_water.py`` script to calculate and return the results.
Simply run the script with this command:
```bash
$ python3 analyze_water.py
```
If done properly, the output should look like this (but with different numbers):
```
Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours
```
> These results show that the average turbidity on the most recent five measurements came out to 1.1992 NTU and since it is over the safe threshold, that being 1.0 NTU, it returns a warning. Lastly, it prints out 8.99 hrs as the minimum time required for the turbidity level to go below the safe threshold.

To run the script with the unit tests, simply run ``pytest``:
```bash
$ pytest
```

If done properly, the output should look like this:
```
================================================= test session starts ==================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/jo25672/homeworkcoe332/homework03
collected 2 items

test_anaylze_water.py ..                                                                                         [100%]

================================================== 2 passed in 0.08s ===================================================
```
> This shows that the two tests in the script ``test_calculate_turbidity`` and ``test_calculate_decay_time`` passed, returning the total time it took to run the tests.

# Accessing the ``turbidity_data.json`` file
> This json file is pulled straight from user **wjallen**'s ``turbidity`` repository located in ``main``.

Firstly, make sure to import the ``requests`` library:
```bash
import requests
```

Then, import the file directly from the site and store it into a variable:
```bash
data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
```

Lastly, make sure to convert it into a **json** format as it will store as **bytes**.
```bash
#simply storing it back into data will make it clean and easy to remember
data = data.json()
```
