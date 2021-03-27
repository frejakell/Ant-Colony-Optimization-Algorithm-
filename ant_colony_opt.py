import numpy as np
import copy

class AntColonyOPT(object):

    def __init__(self, distances,rounds, colony_size, decay_rate, alpha_rate):
        self.distances  = distances
        self.shape=self.distances.shape 
        self.n_cities=self.shape[0]
        self.pheromone = np.empty(self.shape)
        self.colony_size = colony_size
        self.rounds = rounds
        self.decay_rate = decay_rate
        self.alpha_rate = alpha_rate

    def start(self):
        self.pheromone.fill(1/self.n_cities)
        Current_shortest_route = ()
        Final_shortest_route = ( np.inf , np.inf)
        for i in range(self.rounds):
            all_routes = self.ant_tours()
            self.compute_pheronome(all_routes)
            Current_shortest_route = min(all_routes, key=lambda x: x[1])
            Final_shortest_route=min([Final_shortest_route, Current_shortest_route],key=lambda x: x[1])        
            self.Update_pheronome()   
        return Final_shortest_route
       

    def ant_tours(self):
        all_tours = []
        for ant in range(self.colony_size):
            start=0
            tour = []
            visited = []
            visited.append(start)
            Current_pos = start
            
            for i in range(self.shape[0] - 1):
                next_city = self.pick_city(Current_pos, visited)
                tour.append((Current_pos, next_city))
                Current_pos = next_city
                visited.append(next_city)
                
            tour.append((Current_pos, start))
            total_dist = 0
            total_dist=sum(self.distances[ele] for ele in tour)
            all_tours.append((tour,total_dist))
        return all_tours

    def compute_pheronome(self, all_routes):
        sorted_route = sorted(all_routes, key=lambda x: x[1])
        for tour in [s_paths[0] for s_paths in sorted_route]:
            for p in tour:
                pheronome_signal= 1.0 / self.distances[p]
                self.pheromone[p] =self.pheromone[p]+pheronome_signal
                
    def Update_pheronome(self):
        self.pheromone = self.pheromone * self.decay_rate
                        

    def pick_city(self,last_city,visited_cities):
        pheromone=self.pheromone[last_city]
        pheromone = copy.deepcopy(pheromone)
        for city in visited_cities:
            pheromone[city] = 0
        pheromone_props = pow(pheromone,self.alpha_rate)
        moves = np.random.choice(range(self.n_cities), 1, p=(pheromone_props / pheromone_props.sum()))
        return moves[0]
        
distances = np.array([[np.inf, 33, 25, 13, 7, 13],
                      [33, np.inf, 14, 11, 12, 32],
                      
                      [25, 14, np.inf, 10, 24, 10],
                      [13, 11, 10, np.inf, 28, 18],
                      [7, 12, 24, 28, np.inf, 11],
                      [13, 32, 10, 18, 11,np.inf]])
                      
colony_size=100
rounds=50 
beta=0.85
alpha=0.9

ant_colony = AntColonyOPT(distances, rounds, colony_size, beta, alpha)
shortest_path = ant_colony.start()

print ("Best path found:",shortest_path[0])
print ("It has a distance of:", shortest_path[1])