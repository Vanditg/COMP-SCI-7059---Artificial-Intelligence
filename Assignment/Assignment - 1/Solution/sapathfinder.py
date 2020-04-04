//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

import random
from bfs import BFS
import copy
import math
import sys


class SAPathFinder:
    def __init__(self, src, dest, M, N, map_, init_path, t_init, t_fin, alpha, d):
        self.src = src
        self.dest = dest
        self.M = M
        self.N = N
        self.map = map_
        self.p = init_path
        self.t = t_init
        self.t_fin = t_fin
        self.alpha = alpha
        self.d = d
        self.log = []

    def rand_adjust(self):
        random_index = random.randrange(len(self.p))
        u, v = self.p[random_index]
        d_point = random_index + d
        
        if d_point < len(self.p):
            x, y = self.p[d_point]
        else:
            d_point = len(self.p) - 1
            x, y = self.p[-1]
        
        bfs_model = BFS((u, v), (x, y), self.M, self.N, self.map)
        adjusted_path_segment = bfs_model.run(randomized=True)
        
        #ph = self.p.copy()
	ph = copy.copy(self.p)
        j = 0
        for i in range(random_index, d_point+1):
            ph[i] = adjusted_path_segment[j]
            j += 1
        
        return ph

    def calc_cost(self, path):
        cost = 0
        for i in range(1, len(path)):
            x1, y1 = path[i-1]
            x2, y2 = path[i]
            cost += 1 + max(int(self.map[x2][y2]) - int(self.map[x1][y1]), 0)
        
        return cost

    """
    Function for debugging
    """
    def print_path(self, path):
        map_ = copy.deepcopy(self.map)
        for x, y in path:
            map_[x][y] = "*"
    
        for line in map_:
            print(" ".join(line))

    def run(self):
        while self.t > self.t_fin:
            ph = self.rand_adjust()
            g_p = self.calc_cost(self.p)
            g_ph = self.calc_cost(ph)
            delta_g = g_p - g_ph
            self.log.append((self.t, g_p))
            if delta_g > 0:
                self.p = ph
            else:
                prob = math.exp(float(delta_g)/float(self.t))
                if random.random() < prob:
                    self.p = ph
            
            self.t *= self.alpha
        return self.p


if __name__ == '__main__':
    map_file = sys.argv[1]
    init_path_file = sys.argv[2]

    t_init = float(sys.argv[3])
    t_fin = float(sys.argv[4])
    alpha = float(sys.argv[5])
    d = int(sys.argv[6])
    
    file_ = open(map_file)
    path_file = open(init_path_file)

    line = file_.readline()
    line = line.strip().split(" ")
    M, N = int(line[0]), int(line[1])
    src = file_.readline().split()
    src = (int(src[0])-1, int(src[1])-1)
    dest = file_.readline().split()
    dest = (int(dest[0])-1, int(dest[1])-1)

    map_ = []
    for line in file_.readlines():
        line = line.strip().split()
        map_.append(line)

    path_ = []
    for line in path_file.readlines():
        line = line.strip().split()
        path_.append(line)

    init_path = []
    for i in range(len(path_)):
        for j in range(len(path_[0])):
            if path_[i][j] == "*":
                init_path.append((i, j))
    
    sapf = SAPathFinder(src, dest, M, N, map_, init_path, t_init, t_fin, alpha, d)

    fin_path = sapf.run()

    for x, y in fin_path:
        map_[x][y] = "*"
    
    for line in map_:
        print(" ".join(line))
    
    for t, cost in sapf.log:
        print("T = " + "{:.6f}".format(t) + ", cost = " + str(int(cost)))

    file_.close()
    path_file.close()