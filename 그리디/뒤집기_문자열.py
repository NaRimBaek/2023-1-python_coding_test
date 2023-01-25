S = input()
#연속된 0,1 뭉텅기 개수 구하기 둘중에 적은게 답

cnt=0
for i in range(len(S)-1) :
  if S[i] != S[i+1] :
    cnt+=1


print((cnt+1)//2)