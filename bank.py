from decimal import Decimal


def calculate_profit(sum, years):
    for month in range(1, years*12+1):
        intrest = (sum / Decimal('100') * Decimal('17.25')) / Decimal('12')
        tax = intrest / Decimal('100') * Decimal('19.5')
        sum = sum + intrest - tax
        print("Месяц {}: {:.2f}".format(month, sum))
    return sum


a = calculate_profit(Decimal('1800'), 2)
print('{:.2f}'.format(a))
