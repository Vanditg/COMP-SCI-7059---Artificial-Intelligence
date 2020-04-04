//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

from state import State
import random

"""
src - Tuple (x, y)
dest - Tuple (x, y)
returns - Path (as list) 
"""

class BFS:
    def __init__(self, src, dest, M, N, map_):
        self.x0, self.y0 = src
        self.xt, self.yt = dest
        self.M = M
        self.N = N
        self.map = map_
    
    def run(self, randomized=False):
        s = State(self.x0, self.y0)
        
        queue = [s]
        visited = set()
        visited.add((self.x0, self.y0))

        # order = "UDLR"
        # if randomized:
        #     order = ''.join(random.sample(order, len(order)))

        while queue:
            node = queue.pop(0)

            if node.x == self.xt and node.y == self.yt:
                # Reached target destination
                # Backtrack
                path = []
                curr = node
                while curr is not None:
                    path.append((curr.x, curr.y))
                    curr = curr.parent
                return path[::-1]
            
            # Adjustment for randomization
            if not randomized:
                neighbors = node.get_neighbors("UDLR")
            else:
                order = "UDLR"
                random_order = ''.join(random.sample(order, len(order)))
                neighbors = node.get_neighbors(random_order)
            
            for nX, nY in neighbors:
                if (0 <= nX < self.M and 0 <= nY < self.N) and (self.map[nX][nY] != "X") and ((nX, nY) not in visited):
                    nbr_state = State(nX, nY, node)
                    queue.append(nbr_state)
                    visited.add((nX, nY))
        
        return []