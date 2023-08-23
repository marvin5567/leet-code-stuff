# a little bit of an excessive approach to this, but i figured might as well get good with my modules
import math # math cuz its sexy

class Solution:
    def fibo(self, i: int): # this function calculates the fibonacci sequence
        # the equation used here is Binet's formula which is basically this:
        gr = pow((1 + math.sqrt(5))/2, i) # the golden ratio to the power of n; which is defined as i here
        grc = pow((1 - math.sqrt(5))/2, i) # the conjugate of the golden ratio to the power of n

        # both of those are subtracted from each other over the square root of 5
        return math.floor((gr - grc)/math.sqrt(5)) # this is floored to get ints and not floats

    def climbStairs(self, n: int) -> int:
        steps = self.fibo(n) + self.fibo(n - 1) # since the number of steps in the equation is the fibonacci sequence, i just added the current n added to n - 1
        return steps
        # this follows the fn+1 = fn + fn-1 formula
