# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
array_input = input("Enter the array as a list of integers: ")
array = eval(array_input)

if not array or not isinstance(array, list) or not all(isinstance(x, int) for x in array):
    print("Invalid array input")
    exit()

p_input = input("Enter the value of p: ")
p = eval(p_input)

if not isinstance(p, int) or p not in array:
    print("Invalid p input")
    exit()

q_input = input("Enter the value of q: ")
q = eval(q_input)

if not isinstance(q, int) or q not in array:
    print("Invalid q input")
    exit()

# Helper function to construct a BST from a sorted array
def constructBST(array, start, end):
    # If start index is greater than end index, return None
    if start > end:
        return None
    # Find the middle index of the array
    mid = (start + end) // 2
    # Create a new node with the value at the middle index
    node = TreeNode(array[mid])
    # Recursively construct the left subtree from the left half of the array
    node.left = constructBST(array, start, mid - 1)
    # Recursively construct the right subtree from the right half of the array
    node.right = constructBST(array, mid + 1, end)
    # Return the node
    return node

# Construct a BST from the user input array
root = constructBST(array, 0, len(array) - 1)

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # While root is not None or equal to p or q
    while root and root.val != p.val and root.val != q.val:
        # If root value is smaller than both p and q values, LCA is in right subtree
        if root.val < p.val and root.val < q.val:
            root = root.right
        # If root value is larger than both p and q values, LCA is in left subtree
        elif root.val > p.val and root.val > q.val:
            root = root.left
        # Otherwise, root is the LCA
        else:
            break
    # Return root
    return root

# Find and print the LCA of p and q using iteration
lca = lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
print(f"The LCA of {p} and {q} is {lca.val}")
