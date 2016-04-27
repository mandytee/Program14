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
