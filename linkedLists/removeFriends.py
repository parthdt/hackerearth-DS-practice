def solve(size,deletions,friends):
    toDelete = []
    for friend in friends:
        while deletions and toDelete and toDelete[-1]<friend:
            toDelete.pop()
            deletions-=1
        toDelete.append(friend)
    print(*toDelete)

n = int(input())
for _ in range(n):
    size, deletions = map(int,input().split())
    friends = list(map(int,input().split()))
    solve(size,deletions,friends)
