def solve(size):
    arr = []
    for i in range(size):
        arr.append([int(i) for i in list(input())])
    halfSize = size//2 if size%2==0 else (size//2)+1 
    for row in range(halfSize):
        for col in range(halfSize):
            if not (arr[row][col]==arr[size-row-1][col]==arr[row][size-col-1]==arr[size-row-1][size-col-1]):
                return("NO")
    return("YES")


n = int(input())
for _ in range(n):
    size = int(input())
    print(solve(size))
