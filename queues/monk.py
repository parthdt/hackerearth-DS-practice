n = int(input())
call = list(map(int,input().split()))
ideal = list(map(int,input().split()))
count = 0
while len(ideal)!=0:
    if call[0]==ideal[0]:
        call.pop(0)
        ideal.pop(0)
    else:
        call.append(call.pop(0))
    count+=1
print(count)
