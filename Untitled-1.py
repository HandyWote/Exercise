from collections import Counter
n = int(input())
vo = []
for _ in range (n):
    vo.append(input())
    vo.append(vo[-1][0]+vo[-1][-1])
    vo.remove(vo[-2])
ans = 2





print()