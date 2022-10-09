earth_weight = 60

for x in range(0,16):
    moon_weight = (earth_weight + x) * 1.165
    print("달에서의 무게 %s년차 : %s" % (x, moon_weight))