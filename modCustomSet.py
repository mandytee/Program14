"""
Description: will be updated later
"""
_authors_="Amanda Thompson,Dakota Larson,Tenzin"
_date_="4/29/2016"


class CustomSet:
  class CustomSet:
    def __init__(self, ls):
        """
        Description: Instantiates the class
        Precondition: ls, a list
        Postcondition: the list inside the class is set
        """
        self._ls = list()
        for el in ls:
            if not el in self._ls:
                self._ls.append(el)
    def __le__(self, other):
	"""
        Description: checks if one set is a subset of 		another
        Precondition: self, other, both customsets
        Postcondition: None
        """
        for el in self._ls:
            if not el in other._ls:
                return False
        return True
    def __ge__(self, other):
	"""
        Description: checks if one set is a subset of 		another
        Precondition: self, other, both customsets
        Postcondition: None
	"""
        for el in other._ls:
            if not el in other._ls:
                return False
        return True
        
    def lengthMethod(self):
    """
    description- determines the length of the list
    precondition- self must be a list
    postcondition- none
    """
   return len(self._ls)
        
    
    def differenceMethod(self,other):
    """
    description- determines the differnce of two sets
    precondition- self, other must be a list
    postcondition- finalList is the difference
    """
    newList = []
    otherNewList = []
    finalList = []
    for el in self._ls:
        if el not in newList:
            newList.append(el)
    for el in other._ls:
        if el not in otherNewList._ls:
            otherNewList.append(el)
    for el in newList:
        if el not in otherNewList:
            finalList.append(el)
    return finalList
    
    def curlyBracesMethod(self):
    """
    description- Removes the straight brackets from the list and changes them to curly braces
    precondition- self must be a list
    postcondition- Curly braces replace straight brackets
    """
    brace1 = '{'
    comma = ","
    brace2 = "}"
    for el in self._ls:
        brace1 += str(el)
        if el == givenList[-1]:
            brace1 += brace2
        else:
            brace1 += comma
    return brace1

def union(self,ls):
    '''
    Description: adds unique el from the two lists
    Precondition: ls, a list
    Postcondition: changes newList 
    '''
    newList = []
    for el in self._ls:
        if el not in newList:
            newList.append(el)
    
    for el in ls._ls:
        if el not in newList:
            newList.append(el)
    return newList 

def intersection(self,ls):
    '''
    Description: adds el that's common betn the two lists
    Precondition: ls, a list
    Postcondition: changes newList
    '''
    newList = []
    for el in self._ls:
        if el in ls._ls:
            newList.append(el)
    return newList 

def membership(self,ls):
    '''
    Description: checks if ls is in self
    Precondition: ls, a list
    Postcondition: changes newList
    '''
    if ls in self._ls:
        return 'yes'
    else:
        return 'not there'
