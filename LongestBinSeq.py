#2311. Longest Binary Subsequence Less Than or Equal to K
def binToDec(binStr):
    return int(binStr, 2)

def strPop(s, index):
    s = s[:index] + s[index+1:]  # Removes the character at index 1 ('e')
    return s

def longestBinSeq(binStr, k):
    n = len(binStr)
    for i in range(n):
        if binToDec(binStr) <= k:
            break
        if( binStr[i] == '1' ):
            binStr=strPop(binStr, i)
            i+= 1
    return binStr

binStr = input("Enter a binary string: ")
k = int(input("Enter a decimal number k: "))
result = longestBinSeq(binStr, k)
print("Modified binary string:", result)
print("String length: ", len(result))