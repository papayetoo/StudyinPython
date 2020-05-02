import itertools
def isLongPressedName(name, typed):
    g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
    g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
    if len(g1) != len(g2):
        return False

    return all(k1 == k2 and v1 <= v2
               for (k1, v1), (k2, v2) in zip(g1, g2))
print(int('a'))