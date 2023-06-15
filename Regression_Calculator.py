import math

def average(n):
    a = 0
    for i in range(len(n)):
        a = a + n[i]
    b = a / len(n)
    return b

def sd(n):
    a = 0
    b = average(n)
    for i in range(len(n)):
        c = n[i] - b
        c = c ** 2
        a = a + c
    d = a / len(n)
    d = math.sqrt(d)
    return d

def correlation_coefficient(x, y):
    xy = []
    xsq = []
    ysq = []
    for i in range(len(x)):
        xy.append(x[i] * y[i])
        xsq.append(x[i] * x[i])
        ysq.append(y[i] * y[i])
    ex = average(x)
    exsq = average(xsq)
    ey = average(y)
    eysq = average(ysq)
    exy = average(xy)
    a = exy - (ex * ey)
    b = math.sqrt(exsq - (ex ** 2)) * math.sqrt(eysq - (ey ** 2))
    c = a / b
    return c

try:
    a = int(input("Enter the length of the dataset: "))
    b = int(input("Enter the number of independent variables: "))
    x = [[0] * a for _ in range(b)]
    
    for column in range(b):
        for row in range(a):
            x[column][row] = int(input("Enter value for x[{}][{}]: ".format(column, row)))

    print("Enter values for the dependent variable y:")
    y = [0] * a
    for i in range(a):
        y[i] = int(input("Enter value for y[{}]: ".format(i)))

    sdy = sd(y)
    main = [0] * b
    for j in range(b):
        p = [0] * a
        for i in range(b):
            for item in range(a):
                p[item] = x[i][item]
            sdp = sd(p)
            r = correlation_coefficient(p, y)
            c = (r * sdy) / sdp
            main[j] = c

    print("The equation formed is:")
    print("y - {} = ".format(average(y)), end="")
    for j in range(b):
        print("{}x{} - {} ".format(main[j], j, average(x[j])), end="")
    print()

except Exception as e:
    print("An error has occurred:", str(e))
finally:
    print("Program has been completed/terminated")
