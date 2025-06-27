def printKM(n, k):
    for i in range(n+1):
        i+=1
        if kMirrorCheck(i, k):
            print(i, " ", DecToK(i, k))

def DecToK(n, k): #only for base 2 to 10
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k
    digits.reverse()
    return ''.join(str(x) for x in digits)

def reverseString(s):
    return s[::-1]

def kMirrorCheck(n, k):
    ns=str(n)
    if reverseString(ns) == ns and reverseString(DecToK(n, k)) == DecToK(n, k):
        return True
    else:
        return False

limit=int(input("Enter the limit: "))
base=int(input("Enter the base: "))
while(base < 2 or base > 10):
    base=int(input("Base must be between 2 and 10. Enter the base again: "))
printKM(limit, base)