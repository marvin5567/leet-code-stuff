import math
class Solution:
    def fib(self, n: int) -> int:
        gr = pow((1 + math.sqrt(5))/2, n)
        grc = pow((1 - math.sqrt(5))/2, n)
        
        return math.floor((gr - grc)/math.sqrt(5))

# 44 ms runtime
# 16.18 Mbs memory usage
