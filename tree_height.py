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
    def main():
    tree = Tree()
    valid_input = False
    while not valid_input:
        choice = input("Enter 'I' to input from keyboard or 'F' to input from file: ")
        if choice.upper() == 'I':
            n = int(input())
            parent = list(map(int, input().split()))
            tree.build_tree(n, parent)
            valid_input = True
        elif choice.upper() == 'F':
            filename = input("Enter the file name: ")
            if 'a' in filename or 'A' in filename:
                print("Invalid file name. Please enter a file name without the letter 'a'.")
            else:
                try:
                    with open('data/' + filename, 'r') as f:
                        n = int(f.readline())
                        parent = list(map(int, f.readline().split()))
                        tree.build_tree(n, parent)
                        valid_input = True
                except FileNotFoundError:
                    print("File not found. Please enter a valid file name.")
        else:
            print("Invalid choice. Please enter 'I' to input from keyboard or 'F' to input from file.")
    height = tree.compute_height()
    print(height)
    
    root = build_tree(n, parents)
    height = compute_height(root)
    print("Height of the tree is:", height)

if __name__ == '__main__':
    main()
