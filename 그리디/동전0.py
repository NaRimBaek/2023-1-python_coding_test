#동전 0
# 큰 동전이 전부, 작은 동전의 배수가 된다는 뜻
# 그러므로 그리디 알고리즘 사용가능 
N, K = map(int, input().split())

list1=[]
for i in range(N):
  list1.append(int(input()))

list1.sort(reverse=True)
result=0

for i in list1 :
#  if K  > i and K > 0:
  result= result + K //i #몫 =동전 개수
  K = K % i #나머지 

print(result)