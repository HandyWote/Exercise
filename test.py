n = int(input())
a = list(map(int, input().split()))
a.sort()
print(' '.join(map(str, a)))