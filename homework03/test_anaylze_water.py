from analyze_water import calculate_turbidity, calculate_decay_time
import pytest

def test_calculate_turbidity():
    testData = [{'cc': 3, 'dc': 2}, {'cc': 5, 'dc': 6}, {'cc': 2, 'dc': 1}, {'cc': 1.024, 'dc': 2}, {'cc': 2, 'dc': 6}]
    assert round(calculate_turbidity(testData, 'cc', 'dc'), 3) == 10.410

def test_calculate_decay_time():
    assert round(calculate_decay_time(1.1992), 2) == 8.99
    assert calculate_decay_time(0.9852) == 0
