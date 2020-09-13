def height(x):
    if x is None:
        return  0
    return 1 + max(height(x.left),height(x.right))

def dia(x):
    if x is None:
        return 0
    lheight = height(x.left)
    rheight = height(x.right)
    dial=dia(x.left)
    diar=dia(x.right)
    return max(lheight+rheight+1,max(dial,diar))
 
class Node:
    def __init__(self,val,x=None,y=None):
        self.left = x
        self.right = y
        self.val = val
class tree():
    def __init__(self):
        t , x = map(int,input().split())
        root = Node(x)
        for i in range((t-1)):
            com = input()
            val = int(input())
            cur = root
            for x1 in com:
                if x1 == "L":
                    if cur.left is None:
                        cur.left = Node(val)
                    cur=cur.left 
                elif x1 == "R":
                    if cur.right is None:
                        cur.right = Node(val)
                    cur = cur.right
        print(dia(root))
tree()