import itertools
import math
def count_find_num(primesL, limit):
    x = 1
    count = 1
    for i in primesL:
        x *= i
    if x > limit:
        return []
    mx = x
    i = 1
    while 1 == 1:
        A = list(itertools.combinations_with_replacement(primesL, i))
        c = count
        for g in A:
            flag = math.prod(g) * x
            if flag <= limit:
                count += 1
                mx = max(mx, flag)
        if c == count:
            break
        i += 1
    return [count, mx]
