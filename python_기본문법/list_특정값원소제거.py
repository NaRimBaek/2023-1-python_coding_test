#리스트에서 특정 값을 가지는 원소 모두 제거

a=[1,2,3,4,5,5,5]
remove_set={3,5} #제거할 값 
result=[i for i in a if i not in remove_set]
print(result)


