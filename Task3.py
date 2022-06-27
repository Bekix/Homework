#Task 3
def zeros(n):
    if n != 0:
        s = 1
        for i in range(1, n+1):
            s *= i
        count = 0
        i = 1
        while s % 10 ** (count + 1) == 0:
            count += 1
        return count
    else: return 0

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
