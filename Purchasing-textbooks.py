low, r, n = int(input()), int(input()), int(input())
summa = 0
for i in range(1, n + 1):
    a = int(input())
    if low <= a <= r:
        summa += a
print(summa)