n = int(input())
a = set([int(x) for x in input().split()])
a.sort()
b = set([int(x) for x in range(1, max(a) + 1)])
b = list(b - a)
b.sort()
print(b[0] if b else None)