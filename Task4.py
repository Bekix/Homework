#Task 4
def bananas(s) -> set:
    result = set()
    if s == 'banana':
        result.add(s)
    for i in range(len(s)):
        for j in range(i, len(s)):
            for h in range(j, len(s)):
                l = ''
                p = 0
                while p != len(s):
                    if p != i and p != h and p != j:
                        l += s[p]
                    elif p == i:
                        l += '-'
                    elif p == l:
                        l += '-'
                    else:
                        l += '-'
                    p += 1
                string = l
                l = l.replace('-', '')
                if l == 'banana':
                    result.add(string)
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
