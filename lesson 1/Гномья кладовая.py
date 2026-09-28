line = input().split()
chet, nechet = sum(int(el) for el in line if int(el) % 2 == 0), sum(int(el) for el in line if int(el) % 2 != 0)
print(f'Тёмного мёда: {nechet}.\nСветлого мёда: {chet}.')