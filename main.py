
def first(x,y):

    if x < y:
        return y
    else:
        return x

x = int(input("Whats x:"))
y = int(input("Whats y:"))

maxval = first(x,y)

print("The max value is",maxval)

