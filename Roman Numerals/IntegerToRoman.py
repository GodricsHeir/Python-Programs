# File: IntegerToRoman.py
intKey=['I', 'V', 'X', 'L', 'C', 'D', 'M']
romKey=[1,5,10,50,100,500,1000]

def intToRoman(num):
    result = ''
    i = 6  # Start from the largest value (1000)
    if num < 1 or num > 3999:
        return "Input must be between 1 and 3999"
    while num > 0:
       if num//romKey[i] > 0 and num//romKey[i] < 4:
           result += intKey[i] * (num // romKey[i])
           num %= romKey[i]
       elif num // romKey[i] >= 4:
              result += intKey[i]*((num // romKey[i])-3) + intKey[i+1]
              num -= romKey[i+1]-(romKey[i] * ((num // romKey[i])-3))
       else:
            i-=1
    return result

print(intToRoman((int)(input("Enter an integer between 1 and 3999: "))))