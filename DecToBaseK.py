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

n=int(input("Enter a decimal number: "))
k=int(input("Enter the base (2-36): "))
while k < 2 or k > 36:
    print("Base must be between 2 and 36.")
    k = int(input("Enter the base (2-36): "))
print(f"The number {n} in base {k} is: {DecToK(n, k)}")