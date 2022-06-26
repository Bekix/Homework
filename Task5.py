#Task 5
def count_find_num(primesL, limit):
    p = 1
    count = 0
    for i in primesL:
        p *= i
    if p <= limit:
        mx = p
        for n in range(p, limit + 1):
            ans = []
            x = n
            c = 0
            d = 2
            while d ** 2 <= n:
                if n % d == 0:
                    ans.append(d)
                    n //= d
                else:
                    d += 1
            if n > 1:
                ans.append(n)
            if set(ans) == set(primesL):
                count += 1
                mx = max(mx, x)
        return [count, mx]
    else:
        return []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []