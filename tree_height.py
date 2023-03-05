# Emīls Krūmiņš 221RDB241

import sys
import threading
import numpy


def compute_height(x, parent):

    child = {i: [] for i in range(x)}

    root = []
    for i, p in enumerate(parent):
        if p == -1:
            root.append(i)
        else:
            child[p].append(i)

    def find_max_depth(node, mdepth):

        if not child[node]:
            return mdepth
        else:
            d = 0
            for ch in child[node]:
                ch_depth = find_max_depth(ch, mdepth+1)
                d = max(d, ch_depth)
            return d

    height = 0
    for r in root:
        h = find_max_depth(r, 0)
        height = max(height, h)

    return height+1


def main():

    ievade = input()[0]

    if ievade == 'I':
        x = int(input())
        parent = list(map(int, input().split()))
        print(compute_height(x, parent))

    elif ievade == 'F':
        f = input()
        fp = "test/" + f
        if 'a' not in fp:
            with open(fp, 'r') as file:
                print(file.read())
                
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
