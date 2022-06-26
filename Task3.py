#Task 3
def zeros(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    s = str(s)
    count = 0
    for i in range(-1, -len(s)+1, -1):
        if s[i] == '0':
            count += 1
        else:
            break
    return count

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
