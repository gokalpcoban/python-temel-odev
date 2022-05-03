def duz(liste):
    for oge in liste:
        if isinstance(oge , list):
            yield from duz(oge)
        else:
            yield (oge)

liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
duz_liste = [a for a in duz(liste)]

print(duz_liste)
