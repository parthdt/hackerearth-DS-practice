n = int(input())
arr0 = []
arr1 = []
for _ in range(n):
    index,value = map(int,input().split())
    if index==0:
        arr0.append(value)
    else:
        arr1.append(value)
arr0.sort(reverse=True)
arr1.sort(reverse=True)
arr0.extend(arr1)
print(*arr0)

