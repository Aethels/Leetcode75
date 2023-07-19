# A class to represent a node of a binary tree
class Node:
    def __init__(self, val):
        self.val = val # the value of the node
        self.left = None # the left child of the node
        self.right = None # the right child of the node

# A function to build a binary tree from a list
def build_tree(lst, i):
    # Base case: if the index is out of range or the element is None, return None
    if i >= len(lst) or lst[i] is None:
        return None
    # Create a new node with the value at the index
    node = Node(lst[i])
    # Recursively build the left and right subtrees
    node.left = build_tree(lst, 2 * i + 1)
    node.right = build_tree(lst, 2 * i + 2)
    # Return the node
    return node

# A function to invert a binary tree
def invert_tree(node):
    # Base case: if the node is None, return None
    if node is None:
        return None
    # Swap the left and right children of the node
    node.left, node.right = node.right, node.left
    # Recursively invert the left and right subtrees
    invert_tree(node.left)
    invert_tree(node.right)
    # Return the node
    return node

# A function to print the level order traversal of a binary tree
def print_level_order(node):
    # If the node is None, return
    if node is None:
        return
    # Create a queue to store the nodes at each level
    queue = []
    # Enqueue the root node
    queue.append(node)
    # While the queue is not empty
    while queue:
        # Dequeue the first node in the queue
        curr = queue.pop(0)
        # Print its value
        print(curr.val, end=" ")
        # Enqueue its left and right children if they exist
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    # Print a new line
    print()

# Ask the user for an array as input
arr = input("Please enter an array of numbers (or None) to represent a binary tree: ")
# Evaluate the input as a list
lst = eval(arr)
# Build a binary tree from the list
root = build_tree(lst, 0)
# Print the level order traversal of the original tree
print("The original tree is:")
print_level_order(root)
# Invert the binary tree
invert_tree(root)
# Print the level order traversal of the inverted tree
print("The inverted tree is:")
print_level_order(root)
