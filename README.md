# Ant-Colony-Optimization-Algorithm-
Implementation of the ACO algorithm

The ACO algorithm is an  probabilistic-based optimization techique that simulates the foraging behaviour of ants in order to solve a given problem. 
In nature, Ants will use phemone trails in order to signal the best route from the colony to a food source. An overview of the system is summarized below: 

1. As an ant leaves the colony in search for food it leaves behind it a path of phemones.
2. When the ant locates food it will return along the same path that it came.  
3. The phemone will start to evaporate over time so the shorter the path the stronger the scent. 
4. Ants leaving the colony are more likely to follow paths with a stronger scent as this indicates a shorter paths to the food. 

This concept can easily be applied to graph based problems. The code in this project attempts to find the shortest path through a graph which visits each node once along the way 
before returning to the original start node. 

The code consist of a primary class called _ AntColonyOPT_
