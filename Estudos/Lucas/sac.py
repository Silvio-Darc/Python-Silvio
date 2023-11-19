def main(parts, debt, rate):
    amortization = debt / parts
    return sac(parts, debt, rate, 0, amortization)


def sac(parts, debt, rate, interest, amortization):
    if parts == 0:
        return interest
    else:
        new_interest = debt * rate
        new_balance = debt + new_interest
        installment = new_interest + amortization
        new_debt = new_balance - installment
        return sac(parts - 1, new_debt, rate, interest + new_interest, amortization)


assert int(main(120, 300, .00918)) == 166
