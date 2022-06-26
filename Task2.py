#Task 2
def int32_to_ip(int32):
    d = [0, 0, 0, 0]
    d[0] = str(int32 % 256)
    d[1] = str(int32 // 256 % 256)
    d[2] = str(int32 // 256 ** 2 % 256)
    d[3] = str(int32 // 256 ** 3 % 256)
    return d[3] + '.' + d[2] + '.' + d[1] + '.' + d[0]

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
