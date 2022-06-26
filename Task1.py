#Task 1
def domain_name(url):
    c = 0
    while 1 == 1:
        c += 1
        if url[c] == '.': c += 1; break
        if url[c] == '/': c += 2; break
    i = c
    while url[i] != '.': i += 1
    return url[c:i]

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
