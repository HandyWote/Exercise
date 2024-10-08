def count_different_amounts(coins):
    n = len(coins)
    amounts = set()  # 使用集合来存储不同的金额，避免重复

    # 考虑使用0枚、1枚、2枚和3枚硬币的情况
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if i + j + k <= 3:
                    amount = coins[i-1] + coins[j-1] + coins[k-1]
                    if 0 <= i-1 < n and 0 <= j-1 < n and 0 <= k-1 < n:
                        amounts.add(amount if amount > 0 else 0)

    return len(amounts) + 1  # 加1是为了包括0元的情况

# 读取输入
n = int(input())
coins = list(map(int, input().split()))

# 计算并输出结果
print(count_different_amounts(coins))