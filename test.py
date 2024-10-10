n,m,k = map(int,input().split())
g = []
for i in range(n):
    g.append(list(map(int,input().split())))
r = []
for i in range(n):
    for j in range(m):
        if g[i][j]:
            r.append([g[i][j],i + 1,j + 1])
r.sort(reverse=True)
ans = 0
p = [-1,-1]
time = 0
for x,i,j in r:
    if p == [-1,-1]:
        if time + 2 * i + 1 <= k:
            ans += x
            p = [i,j]
            time += i + 1
        else:
            break
    else:
        if time + abs(p[0] - i) + abs(p[1] - j) + i + 1<= k:
            ans += x
            time += abs(p[0] - i) + abs(p[1] - j) + 1
            p = [i,j]
        else:
            break
print(ans)