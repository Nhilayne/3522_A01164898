import math


def CalculateHypotenuse():
    print("Hypotenuse\nPlease enter an x and y length:")
    x = float(input("Length of x: "))
    y = float(input("Length of y: "))
    print("The hypotenuse is %0.2f" % (math.sqrt(x**2 + y**2)))


def add():
    print("Addition x+y\nPlease enter an x and y value:")
    x = float(input("X: "))
    y = float(input("Y: "))
    print("%0.2f + %0.2f = %0.2f" % (x, y, (x + y)))


def subtract():
    print("Subtraction x-y\nPlease enter an x and y value:")
    x = float(input("X: "))
    y = float(input("Y: "))
    print("%0.2f - %0.2f = %0.2f" % (x, y, x - y))


def multiply():
    print("Multiply x*y\nPlease enter an x and y value:")
    x = float(input("X: "))
    y = float(input("Y: "))
    print("%0.2f * %0.2f = %0.2f" % (x, y, x * y))


def divide():
    print("Divide x/y\nPlease enter an x and y value:")
    x = float(input("X: "))
    y = float(input("Y: "))
    print("%0.2f / %0.2f = %0.2f" %(x, y, x / y))


def main():
    print("Please select an option:")
    print("1: Hypotenuse")
    print("2: Addition")
    print("3: Subtraction")
    print("4: Multiplication")
    print("5: Division")
    selection = int(input())
    if selection == 1:
        CalculateHypotenuse()
    elif selection == 2:
        add()
    elif selection == 3:
        subtract()
    elif selection == 4:
        multiply()
    elif selection == 5:
        divide()
    else:
        print("Input not recognized")


if __name__ == "__main__":
    main()
