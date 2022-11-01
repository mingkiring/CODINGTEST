n = input()
score = list(map(int,input().split()))
scoremax= max(score)
sum = sum(score)

print(sum*100/scoremax/int(n))
