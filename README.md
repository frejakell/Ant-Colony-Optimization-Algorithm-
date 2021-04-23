# Ant-Colony-Optimization-Algorithm-
Implementation of the ACO algorithm

The ACO algorithm is an  probabilistic-based optimization techique that simulates the foraging behaviour of ants in order to solve a given problem. 
In nature, Ants will use phemone trails in order to signal the best route from the colony to a food source. An overview of the system is summarized below: 

1. As an ant leaves the colony in search for food it leaves behind it a path of phemones.
2. When the ant locates food it will return along the same path that it came.  
3. The phemone will start to evaporate over time so the shorter the path the stronger the scent. 
4. Ants leaving the colony are more likely to follow paths with a stronger scent as this indicates a shorter paths to the food. 

This concept can easily be applied to graph based problems. The code in this project attempts to find the shortest path through a graph which visits each node once along the way 
before returning to the original start node (the classic traveling salesman problem). 

The code consist of a primary class called _AntColonyOPT_ which takes the following parameters as input:
1. _distance_ : A Distance matrix which provides the distances between nodes in the graph. 
2. _colony_size_ : the number of "ants" in the colony.
3. _rounds_ : The number of times the set of ants will run through the graph
4. _alpha_ : A weight used to tune how most effect the pheromones has on how paths are selected
5. _beta_ : The rate at which the pheromones decay. 

The code return the shortest found path along with the distance of these path. 


