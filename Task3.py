#Task 3
def zeros(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    s = str(s)
    count = 0
    i = 1
    while s % 10 ** i == 0:
        i += 1
        count += 1
    return count

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
