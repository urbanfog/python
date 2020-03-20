def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    def mid(str):
      if len(str) == 1:
        return 0
      elif len(str) % 2 == 0:
        return len(str) // 2 - 1
      else:
        return len(str) // 2
    
    middleIndex = mid(aStr)

    if len(aStr) == 0:
      return False
    elif char == aStr[middleIndex]:
      return True
    elif char > aStr[middleIndex]: # right side
      return isIn(char, aStr[middleIndex + 1:])
    elif char < aStr[middleIndex]: # left side
      return isIn(char, aStr[: middleIndex])
    else:
      return False
    
print(isIn('a', ''))
print(isIn('r', 'gjmmnooopqruuwxy'))