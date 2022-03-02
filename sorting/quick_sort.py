import random


# def partition(ary,l,r):
#     m=l
#     n=l
#     pv = ary[l]
#     for i in range(l+1,r+1):
#         v = ary[i]
#         if v>pv:
#             n+=1
#         else:
#             m+=1
#             ary[i],ary[m]=ary[m],ary[i]
#             n+=1
#     ary[l],ary[m]=ary[m],ary[l]
#     return m

# randomized partition
def partition(ary,l,r):
    pi = random.randint(l,r)
    pv = ary[pi]
    ary[pi],ary[r]=ary[r],ary[pi]
    m = l
    for i in range(l,r):
        if ary[i]<pv:
            ary[i],ary[m]=ary[m],ary[i]
            m+=1
    ary[m],ary[r]=ary[r],ary[m]
    return m
    

def quick_sort(ary,l,r):
    if l<r:
        pi = partition(ary,l,r)
        quick_sort(ary,l,pi-1)
        quick_sort(ary,pi+1,r)

ary = [27,39,12,10]
# partition(ary,0,len(ary)-1)
# print(ary)
quick_sort(ary,0,len(ary)-1)
print(ary)
