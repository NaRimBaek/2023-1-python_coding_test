#5와 6의 차이
n,m = map(str, input().split())

#6을 5로 보면 최소값
minn=int(n.replace("6","5")) + int(m.replace("6","5"))

#5를 6으로 보면 최대값
maxx=int(n.replace("5","6")) + int(m.replace("5","6"))

print(minn, maxx)