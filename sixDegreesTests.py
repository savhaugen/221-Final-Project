"""
Tests the code from sixDegrees
"""
from sixDegrees import *

def test_sixDegrees():

    #Tests valid inputs
    print(BFS('James Duval', 'Meryl Streep'))
    print(BFS('Yoo Ah-in', 'Steven Yeun'))
    print(BFS('Yoo Ah-in', 'Meryl Streep'))
    print(BFS('Kevin Bacon', 'Sean Bean'))

    #Tests same persom
    print(BFS('Yoo Ah-in', 'Yoo Ah-in'))

    #Tests with an invalid input (Savannah Haugen)
    print(BFS('Kevin Bacon', 'Savannah Haugen'))