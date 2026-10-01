from datetime import datetime

# '%d/%m/%Y'
start = datetime.strptime(input(), '%d/%m/%Y')
end = datetime.strptime(input(), '%d/%m/%Y')
delta = end - start
with open('worlds.txt', 'w', encoding='utf-8') as f:
    f.write(f'{delta.days}\n')
    f.write(f'{delta.days * 24}\n')
    if delta.days > 7:
        f.write('Ты стал героем!')
    else:
        f.write('Это было короткое приключение')
