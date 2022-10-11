def moon_weight(earth_weight, increase_amount, year):

    for x in range(1,(year+1)):
        result_weight = (earth_weight + x) * (1 + increase_amount)
        print("달에서의 무게 %s년차 : %s" % (x, result_weight))

moon_weight(90, 0.25, 5)