
def insertion_sort(ary):
    for i in range(1,len(ary)):
        x = ary[i]
        j = i-1
        while j>=0 and ary[j]>x:
            ary[j+1]=ary[j]
            j-=1
        ary[j+1]=x
    return ary
tcs=[
    [5,3,2,6,1,4],
    [1,2,3]
]

for tc in tcs:
    res = insertion_sort(tc)
    print(res)

testary=[5,3,2,6,1,4]
print(list(reversed(testary)))
