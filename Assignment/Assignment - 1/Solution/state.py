//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

class State:
    def __init__(self, x, y, parent=None, cost=0, order=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.order = order
    
    def get_neighbors(self, order):
        order_map = {'U': (self.x - 1, self.y),
                     'D': (self.x + 1, self.y),
                     'L': (self.x, self.y - 1),
                     'R': (self.x, self.y + 1)  
                    }
        neighbors = []
        
        for move in list(order):
            neighbors.append(order_map[move])
        
        return neighbors
    
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.order < other.order
        return self.cost < other.cost