import heapq
def solve(size,walkers):
    kills = 0
    count = 0
    heapq.heapify(walkers)
    while len(walkers)>0:
        walker = heapq.heappop(walkers)
        if walker<=count:
            print("Goodbye Rick")
            print(kills)
            return
        else:
            count+=1
            kills+=1
        if kills%6==0:
            count+=1
    print("Rick now go and save Carl and Judas")
n = int(input())
for _ in range(n):
    size = int(input())
    walkers = list(map(int,input().split()))
    solve(size,walkers)
