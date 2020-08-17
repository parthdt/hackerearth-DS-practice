n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
max  = arr[0]
finalArr = []
finalArr.append(max)
for i in range(1,n):
    if arr[i]>=max:
        max=arr[i]
        finalArr.append(max)
print(*finalArr[::-1])
