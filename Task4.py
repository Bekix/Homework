import itertools

def bananas(s) -> set:
    result = set()
    if s == 'banana':
        result.add(s)
        return result
    A = [i for i in range(len(s))]
    Ar = list(itertools.combinations(A, 6))
    for i in Ar:
        p = ''
        string = ''
        l = [0] * len(s)
        for j in i:
            p += s[j]
        if p == 'banana':
            for g1 in i:
                l[g1] = s[g1]
            for g2 in range(len(l)):
                if l[g2] != 0:
                    string += s[g2]
                else:
                    string += '-'
            result.add(string)
    return result
