romDict={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
IntDict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def romanToInt(s):
    sectors=[]
    j=0
    for i in range(len(s)):
        if i+1<len(s) and IntDict[s[i]]>IntDict[s[i+1]]:
            if(j==0):
                sectors.append(s[:i+1])
            else:
                sectors.append(s[j:i+1])
            j=i+1
        i+=1
    sectors.append(s[j:])
    return sectors

def findLargestInSector(s):
    largest = 0
    for char in s:
        if IntDict[char] > largest:
            largest = IntDict[char]
    ret=romDict[largest]
    return ret

def findSubtractionInSector(s):
    sub=0
    for char in s:
        if IntDict[char] < IntDict[findLargestInSector(s)]:
            sub+=IntDict[char]
    return sub

def findAdditionInSector(s):
    add=0
    for char in s:
        if IntDict[char] >= IntDict[findLargestInSector(s)]:
            add+=IntDict[char]
    return add

def convertToInt(rom):
    sectors = romanToInt(rom)
    total = 0
    index=0
    for i in range(len(sectors)):
        total+= findAdditionInSector(sectors[i]) - findSubtractionInSector(sectors[i])
        index+=1
    return total

roman = input("Enter a Roman numeral: ")
roman = roman.upper()  # Ensure input is uppercase
print(convertToInt(roman))