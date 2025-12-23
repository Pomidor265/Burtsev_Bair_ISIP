# 1

# def N(cur, tar, inc, found=False):
#
#     if cur > tar:
#         return 0
#     if cur == inc:
#         found = True
#
#     if cur == tar and found == True:
#         return 1 if found else 0
#
#     return (N(cur+1, tar, inc, found) + N(cur+2, tar, inc, found) + N(cur*2, tar, inc, found))
#
# res = N(3, 12, 10)
# print(res)

# 2

# def F(cur, tar, forb):
#     if cur > tar:
#         return 0
#     if cur == forb:
#         return 0
#     if cur == tar:
#         return 1
#     return (F(cur+1, tar, forb) + F(2*cur+1, tar, forb))
#
# res = F(1, 27, 26)
# print(res)

# 3

# def S(cur, tar, forb, inc, found=False):
#     if cur > tar:
#         return 0
#     if cur == forb:
#         return 0
#     if cur == inc:
#         found = True
#     if cur == tar and found == True:
#         return 1 if found else 0
#
#     return (S(cur+1, tar, forb, inc, found) + S(cur+2, tar, forb, inc, found))
# res = S(2, 18, 14, 9)
# print(res)