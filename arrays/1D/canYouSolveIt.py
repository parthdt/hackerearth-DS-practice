def solve(size,arr):
    arr1 = [arr[i]+i for i in range(size)]
    arr2 = [arr[i]-i for i in range(size)]
    print(max((max(arr1)-min(arr1)),(max(arr2)-min(arr2))))

n = int(input())
for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    solve(size,arr)

