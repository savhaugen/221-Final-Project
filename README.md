# Six Degrees of Separation
by Rishika Kundu, Savannah Haugen, and Sam Kenney

This project implements the theory of Six Degrees of Separation between actors. It uses an adjancey list to create a graph of actors that are adjacent to each other. Actors are the nodes in the graph, and the movies they are have starred in together are the edges. The program then uses a modified version of the BFS search we learnt in class to find list of actors and movies 2 actors are connected by. 

## Project Contents
sixDegrees.py - contains the source code for our project. The main program will be run from this file

data.csv - data from Kaggle used to create the graph

sixDegreesTests.py - contains the tests for our functions

## How to Use
Make sure the pandas package is installed, as well as the deque and defaultdict package.
Adjust the source data location as needed in line 5. 
Then, run the main function. The program will ask for two actors. Input as prompted, and the terminal will output a list of actors and shared movies. 

