def load_kings(filename):
    kings = []
    with open(filename, 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            if not line.strip():
                continue
            name, start, end = line.strip().split(';')
            kings.append((name.strip(), int(start), int(end)))
    return kings


def century_of(year):
    return (year - 1) // 100 + 1


def duration(start, end):
    return end - start + 1


def filter_by_century(kings, century):
    result = []
    for name, start, end in kings:
        if century_of(start) <= century <= century_of(end):
            result.append(name)
    return sorted(result)


def longest_ruling(kings, n):
    ordered = sorted(kings, key=lambda k: (-duration(k[1], k[2]), k[0]))
    return [name for name, start, end in ordered[:n]]


def report(kings):
    total = len(kings)
    average = sum(duration(start, end) for name, start, end in kings) // total
    longest = longest_ruling(kings, 1)[0]
    return (f'Всего правителей: {total}\n'
            f'Средняя длина правления: {average} лет\n'
            f'Самый долгий правитель: {longest}')


kings = load_kings('cronicle.csv')
print(*filter_by_century(kings, 34), sep=', ')
print(report(kings))