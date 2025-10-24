def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=="" or aStr!=char:
        return False
    m=aStr[len(aStr)/2]
    if char<m:
        aStr=aStr[:len(aStr)/2]
        print aStr
    elif char>m:
        aStr=aStr[len(aStr)/2:]
        print aStr
    return char==m or isIn(char,aStr)
        
