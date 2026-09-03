start, end, rows = int(input()), int(input()), int(input())
first_odd = start
while first_odd <= end:
    if first_odd % 2 == 1:
        break
    first_odd += 1
if first_odd > end:
    exit()
count = 0
current = first_odd
while current <= end:
    count += 1
    current += 2
cols = count // rows
if count % rows != 0:
    cols += 1
row = 0
while row < rows:
    first_in_row = True
    col = 0
    while col < cols:
        idx = col * rows + row
        if idx < count:
            num = first_odd + 2 * idx
            if num <= end:
                if not first_in_row:
                    print("  ", end="")
                print(num, end="")
                first_in_row = False
        col += 1
    print()
    row += 1