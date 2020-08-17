def solve(arr):
    openArr = []
    for char in arr:
        if char in {'{','(','['}:
            openArr.append(char)
        elif not openArr:
            return("NO")
        elif char==')' and openArr[-1]=='(':
            openArr.pop()
        elif char=='}' and openArr[-1]=='{':
            openArr.pop()
        elif char==']' and openArr[-1]=='[':
            openArr.pop()
        else:
            return("NO")
    if openArr:
        return("NO")
    return("YES")
n = int(input())
for _ in range(n):
    print(solve(input()))
    #print(solve(string))
