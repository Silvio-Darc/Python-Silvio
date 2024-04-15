# soma de fracoes
def mdc_f(a, b):
    mdc = 1
    i = 2
    while i < a or i < b:
        if a % i == 0 and b % i == 0:
            mdc = i
        i += 1
    print(f"mdc: {mdc}")
    return mdc


def mmc_f(a, b):
    mdc = mdc_f(a, b)
    mmc = (a / mdc * b / mdc) * mdc
    print(f"mmc: {mmc}")
    return mmc


def soma(a, b, c, d):
    bottom = mmc_f(b, d)
    upper = bottom / b * a + bottom / d * c
    mdc = mdc_f(upper, bottom)

    print(f"{upper / mdc:.0f} {bottom // mdc:.0f}")
    return f"{upper / mdc:.0f} {bottom // mdc:.0f}"


assert mdc_f(4, 6) == 2
assert mdc_f(9, 36) == 9
assert mdc_f(10, 7) == 1
print("")
assert mmc_f(4, 6) == 12
assert mmc_f(9, 36) == 36
assert mmc_f(10, 7) == 70
print("")
assert soma(2, 4, 5, 6) == "4 3"
assert soma(2, 9, 5, 36) == "13 36"
assert soma(3, 10, 5, 7) == "71 70"
