# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    
    heights = [0] * n
    for child_idx in range(n):
        parent_idx = parents[child_idx]
        if parent_idx == -1:
            root = child_idx
        else:
            nodes[parent_idx].append(child_idx)
    def compute_node_height(node_idx):
        if not nodes[node_idx]:
            return 1
        child_heights = [compute_node_height(child_idx) for child_idx in nodes[node_idx]]
        return max(child_heights) + 1
    return compute_node_height(root)

def main():
    # implement input form keyboard and from files
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
