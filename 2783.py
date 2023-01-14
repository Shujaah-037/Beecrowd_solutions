#Cup Stickers
N,C,M = map(int,input().split())
arr1 = list()
arr1 = list(map(int,input().split()))
arr2 = list()
arr2 =list(map(int,input().split()))
c=0
for i in arr1:
    if i not in arr2:
      c+=1 
    else:
      continue
print(c)
