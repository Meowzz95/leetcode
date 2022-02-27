import random
import time

def bubble_sort(ary):
    ll=len(ary)
    for i in range(ll):
        done = True
        for j in range(ll-1):
            if ary[j+1]<ary[j]:
                ary[j+1],ary[j]=ary[j],ary[j+1]
                done = False
        if done:
            break
    return ary


# tcs=[
#     [5,3,2,6,1,4],
#     [1,2,3]
# ]

# for tc in tcs:
#     res = bubble_sort(tc)
#     print(res)

tc = []
for i in range(10**4):
    tc.append(random.randint(0,10**6))

tic = time.perf_counter()
print(bubble_sort(tc))
toc = time.perf_counter()
print(f"bubble sort in {toc - tic:0.4f} seconds")

