#Task 3
def zeros(n):
    count = 0
    while n > 0:
        n /= 5
        count += int(n)
    return count
