"""
Description: This program creates a class CustomSet that contains methods to
determine if a list has the same elements as another list, the length of the list
the difference of two lists, a method to remove the square brackets and replace
them with curly braces, another to join two lists, one to determine what is the
same in two lists, and one to determine if a number is in the list. 
"""
_authors_="Amanda Thompson,Dakota Larson,Tenzin"
_date_="4/29/2016"


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
        Description: checks if one set is a subset of another
        Precondition: self, other, both customsets
        Postcondition: None
        """
        for el in self._ls:
            if not el in other._ls:
                return False
        return True

    def __ge__(self, other):
        """
        Description: checks if one set is a superset of another
        Precondition: self, other, both customsets
        Postcondition: None
        """
        for el in other._ls:
            if not el in self._ls:
                return False
        return True
        
    def __len__(self):
        """
        description- determines the length of the list
        precondition- self must be a list
        postcondition- none
        """
        return len(self._ls)
        
    
    def __sub__(self,other):
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
            if el not in otherNewList:
                otherNewList.append(el)
        for el in newList:
            if el not in otherNewList:
                finalList.append(el)
        return finalList
    
    def __str__(self):
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
            if el == self._ls[-1]:
                brace1 += brace2
            else:
                brace1 += comma
        return brace1

    def or_(self,ls):
        """
        Description: adds unique el from the two lists
        Precondition: ls, a list
        Postcondition: changes newList 
        """
        newList = []
        for el in self._ls:
            if el not in newList:
                newList.append(el)
        
        for el in ls._ls:
            if el not in newList:
                newList.append(el)
        return newList 

    def and_(self,ls):
        """
        Description: adds el that's common between the two lists
        Precondition: ls, a list
        Postcondition: changes newList
        """
        newList = []
        for el in self._ls:
            if el in ls._ls:
                newList.append(el)
        return newList 

    def __contains__(self,num):
        """
        Description: checks if num is in self
        Precondition: self, a list
        Postcondition: none
        """
        if num in self._ls:
            return 'yes'
        else:
            return 'not there'
