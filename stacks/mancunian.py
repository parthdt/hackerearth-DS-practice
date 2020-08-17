def fantabulousCheck(arr):
    index1=arr.index(max(arr))
    M=arr[index1]
    index2=arr.index(max(n for n in arr if n!=M))
    if index2<index1:
        return(index2,index1)

size = int(input())
array = list(map(int,input().split()))
finalSet = set()
subArrays = [array[i:i+j] for i in range(len(array)) for j in range(1,len(array)-i+1)]
for l in subArrays:
    if len(l)>1:
        a = fantabulousCheck(l)
        if a:
            finalSet.add(a)
print(len(finalSet))


