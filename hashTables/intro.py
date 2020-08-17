n = int(input())
a = [None]*(n+1)
for _ in range(n):
    index,element = input().split()
    a[int(index)]=element
q = int(input())
for _ in range(q):
    print(a[int(input())])

