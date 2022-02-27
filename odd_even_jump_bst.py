from typing import List

# AVL tree implementation in Python


import sys


# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def closestValues(root, target):
    larger = float('inf')
    smaller = float('-inf')
    while root:
        if target == root.key:
            return root.key, root.key
        if root.key < target and root.key > smaller:
            smaller = root.key
        if root.key > target and root.key < larger:
            larger = root.key
        if target > root.key:
            root = root.right
        else:
            root = root.left
    return larger, smaller

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        la = len(arr)
        odds = [-1] * la
        evens = [-1] * la
        odds[la - 1] = True
        evens[la - 1] = True
        ind_d = {}
        ind_d[arr[-1]] = la - 1

        root = TreeNode(arr[-1])
        res = 1
        for i in range(la - 2, -1, -1):
            smallest, largest = closestValues(root, arr[i])
            if smallest == float('inf'):
                odds[i] = False
            else:
                smallest_i = ind_d[smallest]
                odds[i] = evens[smallest_i]
                if odds[i]==True:
                    res+=1

            if largest == float('-inf'):
                evens[i] = False
            else:
                largest_i = ind_d[largest]
                evens[i] = odds[largest_i]
            # print(f"current bst, root={root.data}")
            # print(Codec().serialize(root))
            # print(f"for {arr[i]} smallest={smallest} largest={largest}")
            if arr[i] not in ind_d:
                # if val already in tree, we don't need duplicate it
                root = insert(root, arr[i])
            ind_d[arr[i]] = i
        # print("odds",odds)
        # print("evens",evens)
        return res


if __name__ == '__main__':
    tcs = [
        [10, 13, 12, 14, 15],
        [2, 3, 1, 1, 4],
        [5, 1, 3, 4, 2],
    ]
    for tc in tcs:
        print("tc = ", tc)
        print(Solution().oddEvenJumps(tc))
