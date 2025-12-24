#1

# for x in range(15):
#     number1 = 1*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0
#     number2 = 1*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0
#     summ = number1+number2
#     if summ % 14==0:
#         res = summ // 14
#         break
# print(res)

#2

# for p in range(16, 10000):
#     number1 = 10*p**6 + 11*p**5 + 2*p**4 + 6*p**3 + 7*p**2 + 13*p**1 + 1*p**0
#     number2 = 15*p**6 + 0*p**5 + 2*p**4 + 4*p**3 + 10*p**2 + 8*p**1 + 9*p**0
#     summ = number1 + number2
#     if summ % (p-1) == 0:
#         print(p)
#         break

#3

# for x in range(10):
#     number1 = x*17**3 + 11*17**2 + 0*17**1 + 9*17**0
#     number2 = x*15**3 + 8*15**2 + 14*15**1 + 8*15**0
#     summ = number1+number2
#     if summ % 155 ==0:
#         res = summ // 155
#         break
# print(res)

#4

# for x in range(11):
#     for y in range(8):
#         number1 = y*11**4 + 0*11**3 + 4*11**2 + x*11**1 + 5*11**0
#         number2 = 2*8**4 + 5*8**3 + 3*8**2 + x*8**1 + y*8**0
#         summ = number1 + number2
#         if summ % 117 == 0:
#             res = summ // 117
#             print(f"{res}, x= {x}, y= {y}")

#5
number = 7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022
socr_num = oct(number)
print(socr_num.count('7'))