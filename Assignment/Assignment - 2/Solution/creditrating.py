//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 2
//===================================

from __future__ import print_function
import sys
import math


class Node:
    def __init__(self, leaf=False):
        # self.attr = None
        self.splitval = None
        self.leaf = leaf
        self.left = None
        self.right = None
        if leaf:
            self.label = None


def get_unique_labels(data):
    labels = [entry[1] for entry in data]
    labels_counter = {}
    for label in labels:
        labels_counter[label] = labels_counter.get(label, 0) + 1
    return labels_counter


def check_x_equivalence(data):
    X = [tuple(entry[0]) for entry in data]
    X = set(X)
    return len(X) == 1
    

def information_gain(X, idx):
    c1 = X[:idx+1]
    c2 = X[idx+1:]


def entropy(data):
    N = len(data)
    counter = get_unique_labels(data)
    entropy = 0.0
    for label, freq in counter.items():
        p = float(freq) / N
        entropy += - (p * math.log(p, 2))
    return entropy


def choose_split(data):
    n = len(data)
    max_gain = 0
    best_attr = None
    label_entropy = entropy(data)
    for attr in range(len(data[0][0])):
        data.sort(key= lambda x: x[0][attr])
        for i in range(len(data) - 1):
            splitval = 0.5 * (data[i][0][attr] + data[i+1][0][attr])
            px1 = float(i+1)/n
            px2 = float(n - i - 1) / n
            left, right = split_data(data, attr, splitval)
            if len(left) == 0 or len(right) == 0:
                continue
            left_entropy = entropy(left)
            right_entropy = entropy(right)
            gain = label_entropy - (px1 * left_entropy + px2 * right_entropy)
            if gain > max_gain:
                best_attr = attr
                best_split = splitval
                max_gain = gain
    
    return (best_attr, best_split)


def split_data(data, attr, splitval):
    left = []
    right = []
    for entry in data:
        x = entry[0]
        if x[attr] <= splitval:
            left.append(entry)
        else:
            right.append(entry)
    return (left, right)


def dtl(data, minleaf):
    N = len(data)
    labels_count = get_unique_labels(data)
    if N <= minleaf or len(labels_count) == 1 or check_x_equivalence(data):
        leaf_node = Node(leaf=True)
        max_freq = 0
        label = ""
        tie = False
        for l, val in labels_count.items():
            if val > max_freq:
                max_freq = val
                label = l
                tie = False
            elif val == max_freq:
                tie = True
        if not tie:
            leaf_node.label = label
        return leaf_node
    
    attr, splitval = choose_split(data)
    node = Node()
    node.attr = attr
    node.splitval = splitval
    left_data, right_data = split_data(data, attr, splitval)
    node.left = dtl(left_data, minleaf)
    node.right = dtl(right_data, minleaf)
    return node


def predict(node, x):
    while not node.leaf:
        if x[node.attr] <= node.splitval:
            node = node.left
        else:
            node = node.right
    
    return node.label


def print_tree(root, headers):
    queue = [root]
    while len(queue) != 0:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(headers[node.attr] + " " + str(node.splitval) if node.attr is not None else "unknown" + " " + str(node.splitval), end="\t")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()



if __name__ == '__main__':
    train_file_path = sys.argv[1]
    test_file_path = sys.argv[2]
    minleaf = int(sys.argv[3])

    train_file = open(train_file_path)
    test_file = open(test_file_path)

    headers = train_file.readline().strip().split()
    
    train_data = []
    for line in train_file.readlines():
        entry = [float(val) if not val.isalpha() else val for val in line.strip().split()]
        label = entry[-1]
        entry.pop()
        train_data.append((entry, label))

    test_data = []
    test_file.readline() # Skip headers
    for line in test_file.readlines():
        entry = [float(val) for val in line.strip().split()]
        test_data.append(entry)
    
    dtree = dtl(train_data, minleaf)

    for entry in test_data:
        print(predict(dtree, entry))