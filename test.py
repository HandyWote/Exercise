s = input().replace('-', '')  # 移除横杠
a = ''
for i in s:
    if i != 'X':  # 如果不是'X'，则直接添加到字符串a中
        a += i
    else:  # 如果是'X'，则添加字符'X'到字符串a中
        a += 'X'

# 获取最后一位字符
last_char = s[-1]

# 计算加权和
j = 0
for i in range(9):
    j += int(a[i]) * (10 - i)

# 计算包括最后一位的加权和
if last_char == 'X':
    j += 10 * 10  # 如果最后一位是'X'，则乘以10
else:
    j += int(last_char) * 1  # 否则，乘以1

# 计算模11的余数
j = j % 11

# 如果余数为10，将余数设置为'X'
if j == 10:
    j = 'X'

# 比较计算出的余数和最后一位字符
if j == last_char:
    print('Right')
else:
    # 如果不一致，打印修正后的ISBN号
    corrected_isbn = s[:-1] + str(j)
    print(corrected_isbn)