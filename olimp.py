#1

# a = [5, 1, 4, 2, 3, 6]
# N = len(a)
#
# dp = [1] * N
#
# for i in range(N):
#     for j in range(i):
#         if a[j] < a[i] and dp[j] + 1 > dp[i]:
#             dp[i] = dp[j] + 1
#
# max_dlina = dp[0]
# for i in range(1, N):
#     if dp[i] > max_dlina:
#         max_dlina = dp[i]
#
# udalit = N - max_dlina
# print(f"Минимальное число элементов для удаления: {udalit}")

#2
# with open('input.txt', 'r') as f:
#     N = int(f.readline())
#     a = f.readline().split()
#     for i in range(N):
#         a[i] = int(a[i])
#
# dp = [1] * N
#
# for i in range(N):
#     for j in range(i):
#         if a[j] < a[i] and dp[j] + 1 > dp[i]:
#             dp[i] = dp[j] + 1
#
# max_dlina = dp[0]
# for i in range(1, N):
#     if dp[i] > max_dlina:
#         max_dlina = dp[i]
#
# with open("output.txt", "w") as out:
#     out.write(str(max_dlina))

#3

# K = 1050
# count = 0
#
# for x in range(K + 1):
#     n = x
#     n_rev = 0
#
#     while n > 0:
#         number = n % 10
#         n_rev = n_rev * 10 + number
#         n = n // 10
#
#     if x + n_rev == K:
#         count += 1
#
# print(count)



