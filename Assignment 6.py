def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w = w - weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items, dp


def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(i, w):
        if i == 0 or w == 0:
            return 0

        if memo[i][w] != -1:
            return memo[i][w]

        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)
        else:
            include = values[i - 1] + solve(
                i - 1,
                w - weights[i - 1]
            )
            exclude = solve(i - 1, w)
            memo[i][w] = max(include, exclude)

        return memo[i][w]

    maximum_value = solve(n, capacity)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if solve(i, w) != solve(i - 1, w):
            selected_items.append(i)
            w = w - weights[i - 1]

    selected_items.reverse()
    return maximum_value, selected_items


weights = [3, 2, 4, 1]
values = [15, 12, 25, 8]
capacity = 6

print("0/1 KNAPSACK PROBLEM")
print("--------------------")

print("\nItems:")
for i in range(len(weights)):
    print(
        f"Item {i + 1}: Weight = {weights[i]}, "
        f"Value = {values[i]}"
    )

print("\nKnapsack Capacity:", capacity)

value1, items1, dp_table = knapsack_bottom_up(
    weights, values, capacity
)
print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", value1)
print("Selected Items:", items1)

value2, items2 = knapsack_top_down(
    weights, values, capacity
)
print("\n--- Top-Down Approach ---")
print("Maximum Value:", value2)
print("Selected Items:", items2)
