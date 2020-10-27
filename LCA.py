# A recursive python program to find LCA of two nodes
# n1 and n2

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


def treeToString(root: Node, string: list):
    # base case
    if root is None:
        return

    # push the root data as character
    string.append(str(root.data))

    # if leaf node, then return
    if not root.left and not root.right:
        return

    # for left subtree
    string.append('(')
    treeToString(root.left, string)
    string.append(')')

    # only if right child is present to
    # avoid extra parenthesis
    if root.right:
        string.append('(')
        treeToString(root.right, string)
        string.append(')')
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
