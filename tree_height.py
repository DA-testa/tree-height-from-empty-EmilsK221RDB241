import sys
import threading
import numpy

class Node:
    def __init__(self):
        self.children = []

def build_tree(n, parents):
    nodes = [Node() for i in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
    return root

def compute_height(node):
    if len(node.children) == 0:
        return 1
    else:
        heights = []
        for child in node.children:
            heights.append(compute_height(child))
        return max(heights) + 1

def main():
    choice = input("Enter 'I' to input from keyboard or 'F' to input from file: ")
    if choice.upper() == 'I':
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent of each node separated by space: ").split()))
    elif choice.upper() == 'F':
        while True:
            try:
                filename = input("Enter the filename (without letter 'a'): ")
                if 'a' in filename.lower():
                    print("Invalid filename. Try again.")
                else:
                    with open('data/' + filename) as f:
                        n = int(f.readline())
                        parents = list(map(int, f.readline().split()))
                    break
            except FileNotFoundError:
                print("File not found. Try again.")
    else:
        choice = input("Invalid choice. Enter 'I' to input from keyboard or 'F' to input from file: ")
        main()
        return
    
    root = build_tree(n, parents)
    height = compute_height(root)
    print("Height of the tree is:", height)

if __name__ == '__main__':
    main()
