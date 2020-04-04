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

class UniformCostSearch:
    def __init__(self, src, dest, M, N, map_):
        self.x0, self.y0 = src
        self.xt, self.yt = dest
        self.M = M
        self.N = N
        self.map = map_

    def run(self):
        s = State(self.x0, self.y0)
        
        p_queue = [s]
        heapq.heapify(p_queue)
        visited = set()
        visited.add((self.x0, self.y0))
        counter = itertools.count()

        while p_queue:
            node = heapq.heappop(p_queue)

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
                    nbr_state = State(nX, nY, node, cost, next(counter))
                    heapq.heappush(p_queue, nbr_state)
                    visited.add((nX, nY))
        
        return []