#Task1
def domain_name(url):
    url = url.replace('http://', '', 1)
    url = url.replace('https://', '', 1)
    url = url.replace('www.', '', 1)
    i = 0
    ans = ''
    while url[i] != '.':
        ans += url[i]
        i += 1
    return ans
