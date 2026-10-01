from datetime import datetime, timedelta

monthss = [
    "Лев", "Колдунья", "Фавн", "Бобр", "Кентавр",
    "Орланд", "Древо", "Фонарь", "Дуб",
]
holidayss = [
    "День Творения",
    "День Пробуждения",
    "День Даров",
    "День Пророчества",
    "День Возвращения",
]
narniaweekdyas = [
    "Понд", "Вторнд", "Тринд", "Четв",
    "Пятн", "Шестн", "Седьмидень", "Восьмидень",
]
ourweekdays = [
    "Понедельник", "Вторник", "Среда", "Четверг",
    "Пятница", "Суббота", "Воскресенье",
]


def parsing(line):
    line = line.strip()
    if line in holidayss:
        holidayindex = holidayss.index(line) + 1
        doy = 360 + holidayindex
        return doy, holidayindex

    day_str, month_name = line.split(maxsplit=1)
    day = int(day_str)
    monthindex = monthss.index(month_name)
    doy = monthindex * 40 + day
    return doy, None


basedatestr = input().strip()
basedate = datetime.strptime(basedatestr, "%d.%m.%Y")
narnia_date_str = input()
doy, holidayindex = parsing(narnia_date_str)
realdate = basedate + timedelta(days=doy - 1)
if holidayindex is not None:
    narnialine = str(holidayindex)
else:
    weekdayindex = (doy - 1) % 8
    narnialine = narniaweekdyas[weekdayindex]
ourweekday = ourweekdays[realdate.weekday()]
ourline = f"{ourweekday}, {realdate.strftime('%d.%m.%Y')}"
print(narnialine)
print(ourline)
