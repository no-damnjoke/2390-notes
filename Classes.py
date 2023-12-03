class IntSet(object):
    """An intSet is a set of integers"""
    # Information about the implementation (not the abstraction)
    # The value of the set is represented by a list of ints, self.vals. 
    # Each int in the set occurs in self.vals exactly once.

    def __init__(self):
        """Create an empty set of integers""" 
        self.vals = []
        
    def insert(self, e): 
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e): 
        """Assumes e is an integer
           Returns True if e is in return e in self.vals"""
        return e in self.vals
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try: 
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
        
    def getMembers(self):
        """Returns a list containing the elements of self.
           Nothing can be assumed about the order of the elements""" 
        return self.vals[:]

    def __str__(self):
        """Returns a string representation of self""" 
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' #-1 omits trailing comma
    

def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = "Expensive" #description of mortgage
        
    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
        
    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend
    
s = IntSet()
mort = Mortgage(300, 0.03, 6)
print(mort.__str__()) #Output: Expensive