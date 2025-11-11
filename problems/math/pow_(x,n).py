# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# -----------------------------

# parameters - x: int, n: int
# return - value: int

# Q - n can be negative
# Q - x can be negative

# loop n times, multiple x each time. O(n)

# x^n
# x^-n
# x^n -> O(logn)

# x^n = (x^2)^n/2

# 2^2 = 2*2 = 4
# 4^1 = 4
# 2^6 = 2*2*2*2*2*2 = 64
# 4^3 = 4*4*4 = 16 * 4 = 64

# 2^3 = 2*2*2 = 8
# if n is odd -> x^n -> x + (x^2)^n/2
# 2 * 4^1

# x^-n = x^(1/n)

# 2^2 -> 4^1 -> 

# 1 define class
# 2 define method
# 3. if n < 0 -> n = 1/-n
# 4. 
# 5. result = 0 
# 6  while n > 1:
# 7.     add to result value if n is not even, update n to be even, so n-1
# 8.
# 9.     x = x * x
# 10.    n = n//2
# 11. result += x
# 12 return

# Time - O(logn)
# Space - O(1)

class solution:
    def pow(x:int, n:int) -> int:
        if n < 0:
            x = 1/x
            n = -n 
        
        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            
            x *= x
            n //= 2

        return result