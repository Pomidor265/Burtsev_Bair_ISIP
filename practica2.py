#1
"""
with open("39762.txt", "r") as f:
    file = f.readlines()
    file = [int(f) for f in file]
count = 0
max_sum = 0
for i in range(len(file)-1):
    if (file[i] * file[i+1]) % 15 == 0 and (file[i] + file[i+1]) % 7 == 0:
        count += 1
        if max_sum < (file[i] + file[i+1]):
            max_sum = (file[i] + file[i+1])

print(count)
print(max_sum)
"""
#2
"""
with open("68279.txt", "r") as f:
    file = f.readlines()
    file = [int(f) for f in file]
max_n = 0
for n in file:
    if str(n)[-3:] == "562":
        if max_n < n:
            max_n = n
count = 0
max_sum = 0
s = []
for i in range(len(file)-3):
    a = [file[i], file[i+1], file[i+2], file[i+3]]
    more_five = [n for n in a if len(str(n)) == 5]
    not_five = [n for n in a if len(str(n)) != 5]
    krat3 = [n for n in a if n % 3 ==0]
    krat7 = [n for n in a if n % 7 == 0]
    if len(more_five) >=1 and len(not_five) >=2:
        if len(krat3) < len(krat7):
            if sum(a) >  max_n and sum(a) < max_n*2:
                count +=1
                if max_sum < sum(a):
                    max_sum = sum(a)
print(count, max_sum)"""
#3

with open("40992.txt", "r") as f:
    file = f.readlines()
    file = [int(f) for f in file]

count = 0
count_nechet = 0
summ_necget = 0
max_sum= 0
for g in range(len(file)):
    if file[g] % 2 == 1:
        count_nechet +=1
        summ_necget +=file[g]

arg = summ_necget/count_nechet
for i in range(len(file)-1):
    a = file[i]
    b = file[i+1]
    if (a % 5 == 0 or b % 5 == 0) and (a < arg or b < arg):
        count +=1
        if max_sum < (a + b):
            max_sum = (a + b)
print(count, max_sum)