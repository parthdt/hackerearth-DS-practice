n = int(input())
numbers = list(map(int,input().split()))
temp = []
out = []
for number in numbers:
    if number%2 == 0:
        temp.append(number)
    else:
        while len(temp)>0:
            out.append(temp.pop())
        out.append(number)
while len(temp)>0:
    out.append(temp.pop())
print(*out)



