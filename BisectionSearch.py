#Finding Root x

import timeit

def square_root_bisection(x, epsilon, max_steps=1000):
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0

    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if numGuesses > max_steps:
            return(None)
        if ans**2 < x:
            low = ans 
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

print(square_root_bisection(2056, 0.001))


