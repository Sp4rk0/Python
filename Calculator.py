#Calculator
#Enter the first number, then insert the operator and then the second number
print("Enter first number")
n1=float(input())
x=input()
print("Enter second number")
n2=float(input())
if x== "+":
    somma=n1 + n2
    print("= " + str(somma))
elif x== "-":
    meno=n1-n2
    print("= " + str(meno))
elif x== "*":
    per=n1*n2
    print("= " + str(per))
elif x== "/":
    divi=n1/n2
    print("= " + str(divi))