from typing import List


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
        root = Node(arr[-1])

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
            smallest = findMinforN(root, arr[i])

            if smallest == -1:
                odds[i] = False
            else:
                smallest_i = ind_d[smallest]
                odds[i] = evens[smallest_i]

            largest = findMaxforN(root, arr[i])
            if largest == -1:
                evens[i] = False
            else:
                largest_i = ind_d[largest]
                evens[i] = odds[largest_i]
            print(f"current bst, root={root.data}")
            print(Codec().serialize(root))
            print(f"for {arr[i]} smallest={smallest} largest={largest}")
            if arr[i] not in ind_d:
                # if val already in tree, we don't need duplicate it
                root = avl.insert_node(root, arr[i])
            ind_d[arr[i]] = i
        print("odds",odds)
        print("evens",evens)
        res = 0
        for o in odds:
            if o:
                res += 1
        return res

if __name__ == '__main__':
    tcs = [
        [2, 3, 1, 1, 4, 2, 3, 1, 1, 4]
    ]
    for tc in tcs:
        print(Solution().oddEvenJumps(tc))