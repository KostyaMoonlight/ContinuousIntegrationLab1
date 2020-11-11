__version__="1.0.0.0"
from functools import reduce

class TaylorSeries:
    
    def exponential_functionA(self, value):
        return sum([float(value)**n/self.__factorial(n) for n in range(4)])

    def __factorial(self, value):
        return reduce((lambda x,y:x*y),list(range(1,value+1)), 1)
