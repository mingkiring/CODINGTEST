#import sys
#input = sys.stdin.readline
N = int(input())
count = 1 # 본인 N 도 뽑아야하는 경우도 포함되니까 1부터 카운트 시작
start_index =1
end_index = 1
sum = 1

while end_index != N:
    if sum == N:
        count +=1
        end_index +=1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    else :
        end_index += 1
        sum += end_index

print(count)

