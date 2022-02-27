class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def findMinforN(root: Node, N: int):
    # If leaf node reached and is smaller than N
    if root.left is None and root.right is None and root.data < N:
        return -1

    # If node's value is greater than N and left value
    # is NULL or smaller then return the node value
    if root.data >= N and root.left is None or root.data >= N and root.left.data < N:
        return root.data

    # if node value is smaller than N search in the
    # right subtree
    if root.data <= N:
        return findMinforN(root.right, N)

    # if node value is greater than N search in the
    # left subtree
    else:
        return findMinforN(root.left, N)

bst=insert(None,4)
insert(bst,1)
insert(bst,3)

print(findMinforN(bst,2))