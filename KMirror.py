def printKM(n, k):
    for i in range(n+1):
        i+=1
        if kMirrorCheck(i, k):
            print(i, " ", DecToK(i, k))

def DecToK(n, k):
    dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(dictionary[int(n % k)])
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
printKM(limit, base)
