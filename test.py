from collections import Counter

# 假设我们有一个字符串列表
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 使用Counter来计数
counter = Counter(elements)

# 定义一个自定义的顺序
custom_order = ['orange', 'banana', 'apple']

# 根据自定义顺序排序并打印
for element in custom_order:
    if element in counter:
        print(f"{element}: {counter[element]}")