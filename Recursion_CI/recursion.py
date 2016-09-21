def compound_intr(principal, rate, year):
    i = 1
    while year >= i:
        if year == 1:
            return principal * (1 + rate / 100)
        elif year > 1:
            return principal * (1 + rate / 100)**year
        else:
            prev_interest = compound_intr(principal, rate, year - 1) - principal
            interest = prev_interest + principal * (1 + rate / 100)
            return interest
    return year-1

res = compound_intr(100, 10, 1)
print(res)
