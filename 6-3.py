import sys

def moon_weight():
    print('Please enter your current Earth weight')
    earth_weight = int(sys.stdin.readline())

    print('Please enter the amount your weight might increase each year')
    increase_amount = float(sys.stdin.readline())

    print('Please enter the number of years')
    years = int(sys.stdin.readline())

    for x in range(1, (years + 1)):
        result_weight = (earth_weight + x) * (1 + increase_amount)
        print('달에서의 무게 %s 년차 : %s' % (x, result_weight))

moon_weight()