def selection_sort(ary):
    l=0
    while l<=len(ary)-2:
        m=float('inf')
        mi=-1
        for i in range(l,len(ary)):
            if ary[i]<m:
                m=ary[i]
                mi=i
        ary[l],ary[mi]=ary[mi],ary[l]
        l+=1
    return ary

tcs=[
    [5,3,2,6,1,4],
    [1,2,3]
]

for tc in tcs:
    res = selection_sort(tc)
    print(res)
