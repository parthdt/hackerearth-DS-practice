#To return mirror image of given node in the tree, and -1 if no mirror image.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def findMirror(left,right,value):
    if not left or not right:
        return -1
    if left==value:
        return right
    elif right==value:
        return left
    test = findMirror(left.left,right.right,value)
    if test==-1:
        return findMirror(left.right,right.left,value)
    return test


n,q = map(int,input().split())
idk = [Node(i) for i in range(1,n+1)]
for _ in range(n-1):
    parent,value,direction = input().split()
    parent,value = int(parent),int(value)
    if direction=="L":
        idk[parent-1].left = idk[value-1]
    if direction=="R":
        idk[parent-1].right = idk[value-1]
for _ in range(q):
    toFind = int(input())
    if idk[0]==idk[toFind-1]:
        print(idk[0].val)
    else:
        final = findMirror(idk[0].left,idk[0].right,idk[toFind-1])
        if final==-1:
            print(-1)
        else:
            print(final.val)


