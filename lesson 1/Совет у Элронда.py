import json

members = []
with open('members.csv', 'r', encoding='utf-8') as f:
    for el in f:
        members.append(el.strip('\n'))
del members[0]
for i in range(len(members)):
    a = members[i].split(',')
    members[i] = (a[1], a[2])
jsonmembers = {}
for name, race in members:
    jsonmembers.setdefault(race, []).append(name)
with open('council.jsonlines', 'w', encoding='utf-8') as out:
    for race in sorted(jsonmembers):
        names = sorted(jsonmembers[race], key=lambda n: (-len(n), n))
        line = {'race': race, 'members': names}
        out.write(json.dumps(line, ensure_ascii=False) + '\n')