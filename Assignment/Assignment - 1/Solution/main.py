//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

import sys
from pathfinder import PathFinder
import numpy as np

if __name__ == "__main__":
    map_file = sys.argv[1]
    algo = sys.argv[2]
    
    file_ = open(map_file)

    line = file_.readline()
    line = line.strip().split(" ")
    M, N = int(line[0]), int(line[1])
    src = file_.readline().split()
    src = (int(src[0]), int(src[1]))
    dest = file_.readline().split()
    dest = (int(dest[0]), int(dest[1]))

    map_ = []
    for line in file_.readlines():
        line = line.strip().split()
        map_.append(line)

    pf = PathFinder(src, dest, M, N, map_, algo)
    
    path = pf.run()

    for x, y in path:
        map_[x][y] = "*"
    
    print(np.array(map_))