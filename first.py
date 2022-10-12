def main():
    x = int(input("Whats x:?"))
    y = int(input("Whats y:"))

    max(x, y)


def max(x, y):
    if x < y:
        print("Y is great")
    else:
        print("X is great")
