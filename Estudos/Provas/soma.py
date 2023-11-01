a, b, c, d = map(int, input().split())
mmc_embaixo = None
if b % d == 0:
    mmc_embaixo = b
elif d % b == 0:
    mmc_embaixo = d
else:
    mmc_embaixo = d*b
mdc = 1
dividendo = (a*(mmc_embaixo/b) + c*(mmc_embaixo/d))
divisor = mmc_embaixo

if dividendo % divisor == 0:
    mdc = divisor
elif divisor % dividendo == 0:
    mdc = dividendo
else:
    i = 2
    while i < dividendo or i < divisor:
        if dividendo % i == 0 and divisor % i == 0:
            mdc = i
        i += 1
print(f"{dividendo // mdc:.0f} {divisor // mdc}")
