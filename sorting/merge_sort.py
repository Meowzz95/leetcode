import random
import time


def merge(a1,a2):
    i1=0
    i2=0
    res=[]
    while i1<len(a1) and i2<len(a2):
        n1=a1[i1]
        n2=a2[i2]
        if n1<n2:
            res.append(n1)
            i1+=1
        else:
            res.append(n2)
            i2+=1
    while i1<len(a1):
        res.append(a1[i1])
        i1+=1
    while i2<len(a2):
        res.append(a2[i2])
        i2+=1
    return res

def merge_sort(ary):
    if len(ary)==1:
        return ary
    mi = len(ary)//2
    first_half = ary[:mi]
    sec_half = ary[mi:]
    first_half_sorted = merge_sort(first_half)
    sec_half_sorted = merge_sort(sec_half)
    merged = merge(first_half_sorted,sec_half_sorted)
    return merged

# tcs=[
#     [5,3,2,6,1,4],
#     [1,2,3]
# ]
# for tc in tcs:
#     res = merge_sort(tc)
#     print(res)

tc = []
for i in range(10**5):
    tc.append(random.randint(0,10**6))

tic = time.perf_counter()
print(merge_sort(tc))
toc = time.perf_counter()
print(f"merge sort in {toc - tic:0.4f} seconds")
