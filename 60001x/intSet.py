class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self, *vals):
        """Create an empty set of integers"""
        self.vals = list(*vals)

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


    # New code
    def __iter__(self):
        """ Added delegation of iterator to list class """
        return iter(self.vals)

    def intersect(self, s2):
        """ Compares two intSets and returns a new intSet with the elements contained
        in both intSets.
        With no elements in common, an empty intSet is returned.
        """
        return intSet([x for x in list(self) if x in list(s2)])

    def __len__(self):
        """ Returns the nunmber of elements in self"""
        count = 0
        for int in self:
          count += 1
        return count

