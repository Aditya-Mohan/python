from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2+b**2)
print("The length of the hypotenuse is:", c)

a, b, c = map(int, input().split(" "))
if (a**2+b**2 == c**2):
    print("Pythagorus triangle")
else:
    print("Not a pythagorus triangle")
