def computepay(h, g):
    sum = 0
    if h > 40:
        sum = (h - 40)*g*1.5 + 40*g
    else:
        sum = h*g
    return sum

hrs = input("Enter Hours:")
gp = input("Enter gross pay:")
h = float(hrs)
g = float(gp)
p = computepay(h, g)
print("Pay", p)