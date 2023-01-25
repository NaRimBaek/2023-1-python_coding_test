#설탕 배달
n=int(input())
a=[5,3]

result =0 #봉지 수

while n>=0:
  if n%5 ==0 : #5 로 나누어 떨어질때
    result += n//5 #5로 나눈 몫
    print(result)
    break
  n-=3 #5의 배수개 될때까지 3을 빼기
  result+=1 #1번 3을 뺄때 result +1
else :
    print(-1) #




