class Hw1Q2:
    def monomial():
        print ("Solving the monomial")
        a = float(input("Enter a number for a: "))
        b = float(input("Enter a number for b: "))
        c = float(input("Enter a number for c: "))
        x = (c+(2*b))/a
        print(x)

    def polynomial():
        print ("Solving the polynomial")
        a = float(input("Enter a number for a: "))
        b = float(input("Enter a number for b: "))
        c = float(input("Enter a number for c: "))
        x = ((pow(c,2))-(2*b))/a
        print(x)

Hw1Q2.monomial()
Hw1Q2.polynomial()
