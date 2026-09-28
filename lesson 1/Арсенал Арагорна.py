def arsenal(*swords):
    swords = set(swords)
    mlong = sum(len(el) for el in swords) / len(swords)
    return sorted([el.capitalize() for el in swords if len(el) <= mlong])


weapon = ['javelin', 'andurilflameofthewest', 'javelin', 'glamdring', 'breastplate', 'narsil', 'helmet', 'sting',
          'pauldrons', 'dunedainsword', 'scabbard', 'wingedcrown', 'warhammer']
print(*arsenal(*weapon), sep='\n')

# Glamdring
# Helmet
# Javelin
# Narsil
# Pauldrons
# Scabbard
# Sting
# Warhammer
