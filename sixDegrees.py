"""
This program cleans the data from Kaggle, then performs a BFS to return the shortest path between two actors
"""

import pandas as pd
from collections import defaultdict
from collections import deque

# Reads in the data, then isolates the two variables used
movies = pd.read_csv('/Users/rishikakundu/PycharmProjects/testProject/archive/data.csv') #Replace with appropriate location
movies_imp = movies[['Movie Name', 'Stars']].copy()

for index, row in movies_imp.iterrows():
    if isinstance(row['Stars'], str):
        movies_imp.at[index, 'Stars'] = eval(row['Stars'])
    else:
        movies_imp.at[index, 'Stars'] = []

#creates a list of movies and stars, then merges the two
movie_names = list(movies_imp['Movie Name'])
movie_stars = list(movies_imp['Stars'])
movies_dataset = {}
for i in range(len(movie_names)):
    movies_dataset[movie_names[i]] = movie_stars[i]


actorNeighbours = defaultdict(list)


for movie, actors in movies_dataset.items():
    for x in range(len(actors)):
        for y in range(x + 1, len(actors)):
            actor1 = actors[x]
            actor2 = actors[y]

            # Store both the neighbor and the movie that connects them
            if actor2 not in [neighbor[0] for neighbor in actorNeighbours[actor1]]:
                actorNeighbours[actor1].append((actor2, movie))
            if actor1 not in [neighbor[0] for neighbor in actorNeighbours[actor2]]:
                actorNeighbours[actor2].append((actor1, movie))

actorNeighbours = dict(actorNeighbours)


def BFS(source, destination):
    """performs the BFS from actor1 to actor2"""
    queue = deque([[(source, None)]])  # Queue holds paths as lists of tuples (actor, movie)
    visitedNodes = set()

    while queue:
        path = queue.popleft()
        node, movie = path[-1]  # Get the current node and the movie connecting it

        if node in visitedNodes:
            continue
        visitedNodes.add(node)
        if node == destination:
            formatted_path = []
            for i in range(len(path) - 1):
                actor1= path[i][0]
                movie = path[i+1][1]
                actor2 = path[i+1][0]
                formatted_path.append("Actor 1:")
                formatted_path.append(actor1)
                formatted_path.append("Movie:")
                formatted_path.append(movie)
                formatted_path.append("Actor 2:")
                formatted_path.append(actor2)

            return formatted_path

        # Add neighbors to the queue
        for neighbor, connecting_movie in actorNeighbours.get(node, []):
            new_path = list(path)
            new_path.append((neighbor, connecting_movie))
            queue.append(new_path)
    #if actor 2 is not found
    print("Path is not found")
    return False


if __name__ == "__main__":
    actor1 = input("Enter actor 1\n")
    actor2 = input("Enter actor 2\n")
    print(BFS(actor1, actor2))