string01 = 'SF$SDfgsd2eA'
string02 = "64607935616"
string03 = ''
string04 = "Skippy"
string05 = "Nananananananananananananananana Batman!"

def maskify(cc):
    result = '#' * (len(cc)-4) + cc[-4:]
    return result

print(maskify(string01))
print(maskify(string02))
print(maskify(string03))
print(maskify(string04))
print(maskify(string05))