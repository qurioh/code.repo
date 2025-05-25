def squared(x):
    p = x * x
    print(p)
    return p

def area(side):
    squared(side)
    print("Area of square is", squared(side))

s = 25
area(s)

