//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

from state import State
import heapq
import itertools
import math


class AStar:
    def __init__(self, src, dest, M, N, map_, heuristic):
        self.x0, self.y0 = src
        self.xt, self.yt = dest
        self.M = M
        self.N = N
        self.map = map_
        if heuristic == "manhattan":
            self.heuristic = self.manhattan
        elif heuristic == "euclidean":
            self.heuristic = self.euclidean
        else:
            print("Invalid Heuristic! Create new object...")
    
    def manhattan(self, src, dest):
        return abs(src[0] - dest[0]) + abs(src[1] - dest[1])
    
    def euclidean(self, src, dest):
        return math.sqrt((dest[0] - src[0])**2 + (dest[1] - src[1])**2)
    
    def run(self):
        h_root = self.heuristic((self.x0, self.y0), (self.xt, self.yt))
        f_root = h_root
        s = State(self.x0, self.y0)
        
        p_queue = [(f_root, 0, s)]
        heapq.heapify(p_queue)
        visited = set()
        visited.add((self.x0, self.y0))
        counter = itertools.count()
        
        while p_queue:
            f, o, node = heapq.heappop(p_queue)

            if node.x == self.xt and node.y == self.yt:
                # Reached target destination
                # Backtrack
                path = []
                curr = node
                while curr is not None:
                    path.append((curr.x, curr.y))
                    curr = curr.parent
                return path[::-1]
            
            for nX, nY in node.get_neighbors("UDLR"):
                if (0 <= nX < self.M and 0 <= nY < self.N) and (self.map[nX][nY] != "X") and ((nX, nY) not in visited):
                    cost = 1 + node.cost + max(0, int(self.map[nX][nY]) - int(self.map[node.x][node.y]))
                    f_value = cost + self.heuristic((nX, nY), (self.xt, self.yt))
                    order = next(counter)
                    nbr_state = State(nX, nY, node, cost, order)
                    heapq.heappush(p_queue, (f_value, order, nbr_state))
                    visited.add((nX, nY))
        
        return []