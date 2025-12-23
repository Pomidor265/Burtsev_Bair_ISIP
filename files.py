# 1

# with open("27686.txt", "r") as file:
#     f = file.read()
# max_dlina = 0
# cur_dlina = 0
# for i in f:
#     if i == "X":
#         cur_dlina += 1
#     else:
#         cur_dlina = 0
#     max_dlina = max(cur_dlina, max_dlina)
# print(max_dlina)

# 2
# with open("36037.txt", "r") as file:
#     f = file.read()
#
# max_dlina = 0
# cur_dlina = 0
# n = len(f)
#
# for i in range(n):
#     if f[i:i+4] == "XZZY":
#         cur_dlina = 3
#     else:
#         cur_dlina += 1
#     max_dlina = max(max_dlina, cur_dlina)
#
# print(max_dlina)

#3
with open("46982.txt", "r") as file:
    f = file.read()

count = 0
n = len(f)
for i in range(n):
    if f[i] == "E":
        for j in range(i+11, n):
            if f[j] == "E":
                if "F" not in f[i+1:j] and "E" not in f[i+1:j]:
                    count +=1
                break

print(count)