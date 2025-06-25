def choice():
    print("1. Convert from decimal to binary")
    print("2. Convert from decimal to octal")
    print("3. Convert from decimal to hexadecimal")
    print("4. Convert from binary to decimal")
    print("5. Convert from octal to decimal")
    print("6. Convert from hexadecimal to decimal")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary if binary else "0"

def decimal_to_octal(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal if octal else "0"

def decimal_to_hexadecimal(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal if hexadecimal else "0"

def binary_to_decimal(b):
    if not all(c in '01' for c in b):
        raise ValueError("Invalid binary number")
    decimal = 0
    for i, digit in enumerate(reversed(b)):
        decimal += int(digit) * (2 ** i)
    return decimal

def octal_to_decimal(o):
    if not all(c in '01234567' for c in o):
        raise ValueError("Invalid octal number")
    decimal = 0
    for i, digit in enumerate(reversed(o)):
        decimal += int(digit) * (8 ** i)
    return decimal

def hexadecimal_to_decimal(h):
    if not all(c in '0123456789ABCDEF' for c in h):
        raise ValueError("Invalid hexadecimal number")
    decimal = 0
    hex_chars = "0123456789ABCDEF"
    for i, digit in enumerate(reversed(h)):
        decimal += hex_chars.index(digit) * (16 ** i)
    return decimal

c=choice()
while c!=7:
    if c==1:
        n=int(input("Enter a decimal number: "))
        print("Binary: ", decimal_to_binary(n))
    elif c==2:
        n=int(input("Enter a decimal number: "))
        print("Octal: ", decimal_to_octal(n))
    elif c==3:
        n=int(input("Enter a decimal number: "))
        print("Hexadecimal: ", decimal_to_hexadecimal(n))
    elif c==4:
        b=input("Enter a binary number: ")
        print("Decimal: ", binary_to_decimal(b))
    elif c==5:
        o=input("Enter an octal number: ")
        print("Decimal: ", octal_to_decimal(o))
    elif c==6:
        h=input("Enter a hexadecimal number: ")
        print("Decimal: ", hexadecimal_to_decimal(h))
    else:
        print("Invalid choice")
if c==7:
    print("Exiting...")