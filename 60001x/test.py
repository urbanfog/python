def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bDict = {}
    
    if aDict == {}:
        return 'None'
    else:
        for key, value in aDict.items():
            bDict[key] = len(value)
    
    keys = list(bDict.keys())
    values = list(bDict.values())
    result = keys[values.index(max(values))]

    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dingo', 'dog']}

print(biggest(animals))
