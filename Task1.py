#Task 1
def domain_name(url):
    if url[3] == '.':
        c = 4
    else:
        i = 3
        while url[i] != '.' and (url[i - 1] != '/' or url[i] != '/'):
            i += 1
        i += 1
        c = i
    for i in range(c, len(url)):
        if url[i] == '.': v = i; break
    return url[c:v]

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
