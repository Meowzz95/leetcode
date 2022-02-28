# not on leetcode, shopee common interview question
# https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/




# def longest_common_subarray(a1,a2):
#     best=0
#     i1=0
    
#     while i1<len(a1):
#         n1=a1[i1]

#         i2=0
#         while i2<len(a2):
#             n2=a2[i2]
#             if n2==n1:
#                 tmpi1=i1
#                 tmpi2=i2
#                 count=0
#                 while tmpi1<len(a1) and tmpi2<len(a2) and a1[tmpi1]==a2[tmpi2]:
#                     count+=1
#                     tmpi1+=1
#                     tmpi2+=1
#                 best=max(best,count)
#             i2+=1
#         i1+=1

#     return best

import functools


# def longest_common_subarray(a1,a2):
#     @functools.cache
#     def solve(i1,i2):
#         if i1>=len(a1) or i2>=len(a2):
#             return 0
#         count=0
#         if a1[i1]==a2[i2]:
#             while i1<len(a1) and i2<len(a2) and a1[i1]==a2[i2]:
#                 count+=1
#                 i1+=1
#                 i2+=1
#             # ignore = solve(i1+count,i2+count)
#             # return max(count,ignore)
#         ignore1 = solve(i1+1,i2)
#         ignore2 = solve(i1,i2+1)
#         return max(count,ignore1,ignore2)
#     return solve(0,0)

# def longest_common_subarray(a1,a2):
#     @functools.cache
#     def solve(i1,i2,best):
#         if i1>=len(a1) or i2>=len(a2):
#             return best
#         if a1[i1]==a2[i2]:
#             return solve(i1+1,i2+1,best+1)
        
#         res= max(solve(i1+1,i2,0),solve(i1,i2+1,0))
#         return max(best,res)
#     return solve(0,0,0)

def longest_common_subarray(a1,a2):
    dp=[]
    for r in range(len(a1)+1):
        tmp=[]
        for c in range(len(a2)+1):
            tmp.append(0)
        dp.append(tmp)
    best=0
    for r in range(len(a1)-1,-1,-1):
        for c in range(len(a2)-1,-1,-1):
            if a1[r]==a2[c]:
                dp[r][c]=dp[r+1][c+1]+1
                best=max(best,dp[r][c])
    return best
    
        

tcs = [
    [[1, 2, 8, 2, 1],[8, 2, 1, 4, 7],3],
    [[1, 2, 8, 3, 2, 1],[8, 2, 1, 4, 7],2],
    [[1, 2, 3, 2, 1],[8, 7, 6, 4, 7],0],
    [[1,1,1,1,1],[1,1,1,1,1],5]
]
for tc in tcs:
    res = longest_common_subarray(tc[0],tc[1])
    print(res,res==tc[2])
