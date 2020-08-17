n = int(input())
a = []
for _ in range(n):
    toDo = input()
    if toDo[0] =='E':
        a.append(int(toDo.split()[1]))
        print(len(a))
    elif len(a)>0:
        print(a.pop(0),len(a))
    else:
        print("-1 0")
