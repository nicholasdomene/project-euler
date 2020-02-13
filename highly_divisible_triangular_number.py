import math

def divisors(n):
    div = []
    sqrt = int(math.sqrt(n))
    for i in range(1, sqrt+1):
        if n%i == 0:
            div.append(i)
    return div

j = 1
k = 1
max_divs = 1
while max_divs < 500:
    k += 1
    j += k
    divs = len(divisors(j))*2
    if divs > max_divs:
        max_divs = divs
        print(max_divs)

print(j)
