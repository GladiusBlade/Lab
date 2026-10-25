N = int(input())
h = (N // 3600) % 24
m = (N // 60) % 60
s = N % 60
print("{}:{}:{}".format(h, format(m, "02"), format(s, "02")))
