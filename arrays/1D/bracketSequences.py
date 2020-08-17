bs = input()
newdict = {}
ps = 0
for bracket in bs:
    ps+= 1 if bracket == '(' else -1
    newdict[ps] = newdict.get(ps,0) + 1
print(newdict[sorted(newdict)[0]])

