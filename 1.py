 #!/usr/bin/env python
print(""""********************
This program helps to find the roots of a second-order equation
a=x-squared term
b=x coefficient term
c=invariable 

*******************
""")
a=int(input("Please enter a:"))
b=int(input("Please enter b:"))
c=int(input("Please enter c:"))
discriminant=b**2-4*a*c

if discriminant<0:
    print("Real root does not exist!")


elif discriminant==0:
    print("quadratic has a repeated real number solution")
    print("x1==", (-b - discriminant ** 1 / 2) / 2 * a, ",", "x2==", (-b + discriminant ** 1 / 2) / 2 * a)

else:
    print("the quadratic has two distinct real number solutions")
    print("x1==", (-b - discriminant ** 1 / 2) / 2 * a, ",", "x2==", (-b + discriminant ** 1 / 2) / 2 * a)

