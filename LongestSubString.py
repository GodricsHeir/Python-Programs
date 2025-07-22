def checkPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

subColletion = []

def largestInList(subCollection):
    if not subCollection:
        return ""
    largest = subCollection[0]
    for item in subCollection:
        if len(item) > len(largest):
            largest = item
    return largest

def longestPalindrome(s):
    limit = len(s)
    while limit > 0:
        limit-=1
        for i in range(len(s) - limit):
            substring = s[i:i + limit + 1]
            if checkPalindrome(substring):
                subColletion.append(substring)
    if len(largestInList(subColletion))>1:
        return largestInList(subColletion)
    else:
        return "No Palindrome Found"
    
print(longestPalindrome(input("Enter a string: "))) 

