from typing import List

# AVL tree implementation in Python


import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

def closestValueLarger(root, target) -> int:

    gap = float('inf')
    res = float('inf')
    while root:
        if target == root.key:
            return root.key
        if root.key>target:
            g = abs(target - root.key)
            if g < gap:
                gap = g
                res = root.key
        if target > root.key:
            root = root.right
        else:
            root = root.left
    return res

def closestValueSmaller(root, target) -> int:

    gap = float('inf')
    res = float('inf')
    while root:
        if target == root.key:
            return root.key
        if root.key<target:
            g = abs(target - root.key)
            if g < gap:
                gap = g
                res = root.key
        if target > root.key:
            root = root.right
        else:
            root = root.left
    return res


# myTree = AVLTree()
# root = None
# nums = [33, 13, 52, 9, 21, 61, 8, 11]
# for num in nums:
#     root = myTree.insert_node(root, num)
# myTree.printHelper(root, "", True)
# key = 13
# root = myTree.delete_node(root, key)
# print("After Deletion: ")
# myTree.printHelper(root, "", True)

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        la = len(arr)
        odds = [-1] * la
        evens = [-1] * la
        odds[la - 1] = True
        evens[la - 1] = True
        ind_d = {}
        ind_d[arr[-1]] = la - 1

        avl = AVLTree()
        root = TreeNode(arr[-1])

        for i in range(la - 2, -1, -1):
            # smallest=float('inf')
            # smallest_i=-1
            # largest=float('-inf')
            # largest_i=-1
            # for j in range(i+1,la):
            #     if arr[i]<=arr[j] and arr[j]<smallest:
            #         smallest=arr[j]
            #         smallest_i=j
            #     if arr[i]>=arr[j] and arr[j]>largest:
            #         largest=arr[j]
            #         largest_i=j
            smallest = closestValueLarger(root, arr[i])

            if smallest == float('inf'):
                odds[i] = False
            else:
                smallest_i = ind_d[smallest]
                odds[i] = evens[smallest_i]

            largest = closestValueSmaller(root, arr[i])
            if largest == float('inf'):
                evens[i] = False
            else:
                largest_i = ind_d[largest]
                evens[i] = odds[largest_i]
            # print(f"current bst, root={root.data}")
            # print(Codec().serialize(root))
            # print(f"for {arr[i]} smallest={smallest} largest={largest}")
            if arr[i] not in ind_d:
                # if val already in tree, we don't need duplicate it
                root = avl.insert_node(root, arr[i])
            ind_d[arr[i]] = i
        # print("odds",odds)
        # print("evens",evens)
        res = 0
        for o in odds:
            if o:
                res += 1
        return res

if __name__ == '__main__':
    tcs = [
        [10, 13, 12, 14, 15],
        [2, 3, 1, 1, 4],
        [5, 1, 3, 4, 2],
    ]
    for tc in tcs:
        print("tc = ",tc)
        print(Solution().oddEvenJumps(tc))
