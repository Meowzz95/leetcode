class Solution:
    def countPrimes(self, n: int) -> int:
        # if n is 10, marks = 0-9, where 0 and 1 are init as false (0 is not used, 1 is not prime)
        marks = [False]*2+[True]*(n-2)
        # print(marks)
        i=2
        while(i*i<n):
            if marks[i]==False:
                i += 1
                continue
            j = i*i
            while(j<n):
                marks[j]=False
                j+=i
            i+=1
            print("i",i)
            print(marks)
        # print(marks)
        count = 0
        for m in marks:
            if m:
                count+=1
        return count

if __name__ == '__main__':
    print(Solution().countPrimes(10000))