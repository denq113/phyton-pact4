i = 0
g = 1000
d = g
while(i<10):
    if (int(str(g)[:3])==100):
        if (g % 9 == 0):
            h = g
            h = h % 10
            if (h == 7):
                print(g)
                i = i + 1
    g = g + 1