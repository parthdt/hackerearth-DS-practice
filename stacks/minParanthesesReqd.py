string = input()
openArr = []
closeCount = 0
for char in string:
    if char=='(':
        openArr.append(char)
    elif char==')' and openArr:
        openArr.pop()
    else:
        closeCount+=1
print(len(openArr)+closeCount)
