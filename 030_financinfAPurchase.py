# rate = 7.4
# bal = 10215
# term = 24
# num_payments = 20

def amort(rate, bal, term, num_payments):
    print(rate)
    monthlyRate = rate/100/12
    print(monthlyRate)
    n = rate * bal
    d = 1 - (1 + rate) ** (- term)
    c = n / d

    return print("num_payment %d c %.0f princ %.0f int %.0f balance %.0f")

print(amort(7.4, 10215, 24, 20))