#보물
#B는 정렬하면 안된다
#A는 오름차순으로 정렬해주고, b는 pop을 이용해 최대값부터 뽑는다 

N=int(input())

A=list(map(int, input().split()))
B=list(map(int, input().split()))
result=0
A.sort()

for i in range(N):
  x=A[i]
  y=B.pop(B.index(max(B)))
  result += x*y

print(result)


