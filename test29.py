N = int(input())
A = list(map(int,input().split()))
M = int(input())
target_list = list(map(int,input().split()))
A.sort() #A를 오름차순으로 정렬

for i in range(M):
    find = False #find를 false로 먼저 초기화
    targetdata = target_list[i]
    #이진탐색 시작
    start = 0
    end = len(A) - 1
    while start<=end:
        midindex = int((start+end)/2)
        midvalue = A[midindex]
        if midvalue > targetdata:
            end = midindex -1
        elif midvalue < targetdata:
            start = midindex + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)
