import csv
#Монетки
"""
with open ("36031.csv", "r") as f:
    n = list(csv.reader(f))
l = []
path = []
for i in range(len(n)):
    a = (n[i][0].split(";"))
    a = [int(el) for el in a]

    l.append(a)
l = l[-1::-1]

for e in range(len(l)):
    for j in range(len(l[e])):
        if j == 0 and e == 0:
            continue
        elif e == 0 and j != 0:
            l[e][j] = l[e][j]+l[e][j-1]

        elif e != 0 and j == 0:
            l[e][j] = l[e][j]+l[e-1][j]
        else:
            l[e][j] = max(l[e-1][j], l[e][j-1]) + l[e][j]
print(l[-1][-1])
s = ""
for e in range(len(l)):
    for j in range(len(l[e])):
        if e == 0 and j != 0:
            s = "left"
        elif e != 0 and j == 0:
            s = "up"
        else:
            if l[e-1][j] > l[e][j-1]:
                s = "up"
            elif l[e][j-1] > l[e-1][j]:
                s = "left"
        path.append(s)

p = []
i = len(l)-1
j = len(l[0])-1
while i > 0 or j > 0:
    if i ==0:
        j -=1
        p.append("left")
    elif j == 0:
        i -=1
        p.append("up")
    else:
        if l[i - 1][j] > l[i][j - 1]:
            i -= 1
            p.append("up")
        elif l[i][j - 1] > l[i - 1][j]:
            j -=1
            p.append("left")
p = p[::-1]
print(p)
"""

#1
"""
with open("59778.csv", "r") as file:
    file = list(csv.reader(file))
l = []
for i in range(len(file)):
    a = (file[i][0].split(";"))
    a = [int(el) for el in a]
    l.append(a)
#print(l[14].count(l[14][0]))
count = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i].count(l[i][j]) == 4:
            repeat = l[i][j]
            x = []
            for j in range(len(l[i])):
                if l[i][j] not in x and l[i][j] != repeat:
                    x.append(l[i][j])
            summa_repeat = 4*repeat
            average_sum = sum(x) / len(x)
            if average_sum > summa_repeat:
                count +=1
print(count//4)
"""
#2

with open("29666.csv", "r") as file:
    fi = csv.reader(file, delimiter=";")
    l = []
    for i in fi:
        a = i[0].replace(",", ".")
        l.append(float(a))

print(l)
max_sum = 0
for i in range(len(l)):
    j_max = l[i]
    for j in range(i+1, len(l)):
        if l[j] < l[j-1]:
            j_max += l[j]
        else:
            break
    if max_sum < j_max:
        max_sum = j_max
print(max_sum)

