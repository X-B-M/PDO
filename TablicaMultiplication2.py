x1 = 15
x2 = 30
y1 = 28
y2 = 41
prnStr = "   "
for i in range(x1, x2 + 1):
    prnStr += "%5d" % (i)
print(prnStr)

for i in range(y1, y2 + 1):
    prnStr = "%3d" % (i)
    for j in range(x1, x2 + 1):
        if (i * j) % 10 == 0:
            prnStr += "\033[33m"
        if i == j:
            prnStr += "\033[1m"

        prnStr += "%5d" % (i * j) + "\033[0m"
    print(prnStr)

