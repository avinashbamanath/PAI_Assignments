def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]


sequence1 = input("Enter first sequence: ")
sequence2 = input("Enter second sequence: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLCS:", lcs)
print("LCS Length:", length)

