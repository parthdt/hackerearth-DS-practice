n = int(input())
for _ in range(n):
    needle = input()
    haystack = input()
    if needle in haystack or needle[::-1] in haystack:
        print("YES")
    else:
        print("NO")

