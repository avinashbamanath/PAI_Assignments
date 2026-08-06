
def fib_memo(num, cache=None):
    if cache is None:
        cache = {}

    if num in cache:
        return cache[num]

    if num <= 1:
        return num

    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]


def fib_tab(num):
    if num <= 1:
        return num

    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    print("Generated Series:", table)
    return table[num]


def fib_optimized(num):
    if num <= 1:
        return num

    prev, curr = 0, 1
    for _ in range(2, num + 1):
        prev, curr = curr, prev + curr
    return curr


n = int(input("Enter position of Fibonacci number: "))

memo_result = fib_memo(n)
tab_result = fib_tab(n)
opt_result = fib_optimized(n)

print("\nMemoization Result :", memo_result)
print("Tabulation Result  :", tab_result)
print("Optimized DP Result:", opt_result)






# Enter position of Fibonacci number: 10
# Generated Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Memoization Result : 55
# Tabulation Result  : 55
# Optimized DP Result: 55