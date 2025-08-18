n = int(input())
i = int(1)
res = 0
while True:
    temp = int(n // 5**i)
    res += temp
    i += 1
    if temp == 0:
        break
print(res)