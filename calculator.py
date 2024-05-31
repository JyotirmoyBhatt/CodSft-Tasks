import math

def sum(a, b):
    a += b
    return a

def sub(a, b):
    if a > b:
        a -= b
        return a
    else:
        b -= a
        return b

def mul(a, b):
    a *= b
    return a

def div(a, b):
    q = a / b
    r = a % b
    return q, r

print("Calculator")

while True:
    print("\nChoose the operation to be performed")
    print("\n\t1. Addition")
    print("\n\t2. Subtraction")
    print("\n\t3. Multiplication")
    print("\n\t4. Division")
    print("\n\t5. Exit")

    choice = int(input('> '))

    if choice == 1:
        print("\nEnter 2 numbers: ")
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        result = sum(n1, n2)
        print("\nThe sum is: %s" % result)

    elif choice == 2:
        print("\nEnter 2 numbers: ")
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        result = sub(n1, n2)
        print("\nThe difference is: %s" % result)

    elif choice == 3:
        print("\nEnter 2 numbers: ")
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        result = mul(n1, n2)
        print("\nThe product is: %s" % result)

    elif choice == 4:
        print("\nEnter 2 numbers: ")
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        q, r = div(n1, n2)
        print("\nThe quotient is: %s" % q)
        print("The remainder is: %s" % r)

    elif choice == 5:
        print("\nExit")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")
