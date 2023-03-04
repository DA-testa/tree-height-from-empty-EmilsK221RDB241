import sys
import threading
import numpy

class nodes:
    def __init__(self, parent, child=None):
        self.parent = parent
        self.child = child
        
    def addChild(self, node):
        if self.child is None:
            self.child = []
        self.child.append(node)

def compute_height(n, parents):
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def maxDepth(node):
    if node.child is None:
        return 0
    children = node.child
    depth_list = []
    for child in children:
        depth_list.append(maxDepth(child))
    return max(depth_list, default=0) + 1

def input_from_keyboard():
    n = int(input().strip())
    parents = list(map(int, input().split()))
    return n, parents

def input_from_file():
    filename = input("Enter filename (without extension): ")
    while not re.match(r'^[^aA]*$', filename):
        filename = input("Invalid filename. Enter filename (without extension): ")
    try:
        with open(os.path.join('input_files', f"{filename}.txt"), 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().split()))
    except FileNotFoundError:
        print("File not found.")
        return None, None
    return n, parents

def main():
    try:
        choice = input("Enter 'I' to input from keyboard or 'F' to input from file: ")
        while choice not in ('I', 'F'):
            choice = input("Invalid choice. Enter 'I' to input from keyboard or 'F' to input from file: ")
             
    input_methods = {
        'I': input_from_keyboard,
        'F': input_from_file,
    }

    choice = input("Enter 'I' to input from keyboard or 'F' to input from file: ")
    while choice not in input_methods:
        choice = input("Invalid choice. Enter 'I' to input from keyboard or 'F' to input from file: ")

    n, parents = input_methods[choice]()

    if n is None or parents is None:
        return

    nodes_list = []
    for i in range(n):
        nodes_list.append(nodes(parents[i]))
        
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes_list[parent_index].addChild(nodes_list[child_index])
    
    if len(nodes_list) == 0:
        return 0
    
    height = maxDepth(nodes_list[root]) + 1
    
    print(height)
    return 0   
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
