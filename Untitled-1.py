m = [int(i) for i in range(1,2025)]
m1 =[]
for i in range(len(m)):
    for j in range(i,len(m)):
        m1.append(m[i]+m[j])
print(sort)