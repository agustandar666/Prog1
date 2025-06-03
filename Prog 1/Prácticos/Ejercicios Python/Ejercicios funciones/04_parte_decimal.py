def parte_decimal(n):
    p_decimal = n - int(n)
    return round(p_decimal, len(str(n)) - 2)


print(parte_decimal(21.32))
