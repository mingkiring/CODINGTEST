N = int(input())
A = [0]*N #수열 초기화

for i in range(N):
    A[i] = int(input())

#스택
stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else :
        n = stack.pop()
        if n > num:
            print("NO")
            result = "FALSE"
            break
        else:
            answer +="-\n"

if result :
    print(answer)