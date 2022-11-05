import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int,input().split()))
A.sort() #오름차순을 정렬

for K in range(N):
    find = A[K]
    i = 0
    j = N -1
    while i<j:
        ## 이 부분 알고리즘 빼먹지 않기 i,j 가 k 아닐 경우에 좋은 수임!
        if A[i]+A[j] == find:
            if i != K and j!= K:
                Result +=1
                break
            elif i == K:
                i +=1
            elif j== K:
                j -=1
        elif A[i]+A[j] > find:
            j -= 1
        else:
            i += 1
print(Result)