class Node:
    def __init__(self,val=None,ne=None):
        self.val=val
        self.ne=ne


def merge(l, r):
    dummy = Node()
    cur = dummy
    while l and r:
        if l.val<r.val:
            cur.ne = l
            cur = cur.ne
            l=l.ne
        else:
            cur.ne = r
            cur = cur.ne
            r=r.ne
    while l:
        cur.ne=l
        cur=cur.ne
        l=l.ne
    while r:
        cur.ne=r
        cur=cur.ne
        r=r.ne
    return dummy.ne



def merge_sort(root:Node):
    if not root.ne:
        return root

    l = root
    r = find_middle(root)
    l = merge_sort(l)
    r = merge_sort(r)
    return merge(l,r)

def find_middle(root:Node):

    slow=root
    fast=root.ne
    while fast and fast.ne:
        slow=slow.ne
        fast=fast.ne.ne
    middle_head=slow.ne
    slow.ne=None
    return middle_head

def print_sll(node:Node):
    while node:
        print(node.val)
        node=node.ne
print_sll(merge_sort(Node(2,Node(88,Node(1,Node(99,Node(5)))))))