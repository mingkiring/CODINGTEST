#버블 정렬
#N개의 숫자를 입력 받고, 오름차순으로 정렬하기
# sort 함수를 이용할수 있지만 , 버블정렬을 이용해서 풀기
N = int(input())
A = [0]*N # A 리스트 초기화
for i in range(N):
    A[i] = int(input()) #A 리스트 수 입력 받기

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

#print(A) : 이건 리스트로 출력되는 것
for i in range(N):
    print(A[i])
#이건 정렬된 숫자로 하나씩 출ㄹ력