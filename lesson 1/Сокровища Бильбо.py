import json


def process_treasures(csv_filename, json_filename, secret_key, grouping):
    with open(csv_filename, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split('.')
        rows = []
        for line in f:
            if line.strip():
                rows.append(line.strip().split('.'))

    total_quantity = sum(int(row[1]) for row in rows)
    if total_quantity != secret_key:
        with open(json_filename, 'w', encoding='utf-8') as out:
            json.dump({"error": "access denied"}, out, ensure_ascii=False, indent=2)
        return

    ru_names = ['Предмет', 'Количество', 'Цена_в_золотых', 'Где_найдено']
    if grouping in header:
        idx = header.index(grouping)
    else:
        idx = ru_names.index(grouping)

    groups = {}
    for row in rows:
        groups.setdefault(row[idx], []).append(row)

    def group_order(value):
        return (0, int(value), '') if value.isdigit() else (1, 0, value)

    result = {}
    for value in sorted(groups, key=group_order):
        items = groups[value]
        result['group' + value] = {
            'total_items': sum(int(r[1]) for r in items),
            'total_value': sum(int(r[1]) * int(r[2]) for r in items),
            'items': sorted((r[0] for r in items), reverse=True),
        }

    with open(json_filename, 'w', encoding='utf-8') as out:
        json.dump(result, out, ensure_ascii=False, indent=2)


process_treasures('treasure.csv', 'result.json', 19, 'Quantity')
