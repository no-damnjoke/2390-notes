import timeit

#Ranked by efficiency in descencing order

def normalSquareRoot(x, epsilon, max_steps = 1e8): #Don't set max_steps or set max_step extremely high
    step = epsilon**2 
    numGuesses = 0
    ans = 0.0

    while abs(ans**2 - x) >= epsilon:
        ans += step
        numGuesses += 1
        if numGuesses > max_steps:
            return None
    return ans

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

def square_root_newton(k, epsilon, max_steps=1000):    
    guess = k/2.0
    steps = 0
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (((guess**2) - k)/(2*guess)) 
        steps = steps + 1
        if steps > max_steps:
            return None
    return guess


x = 15
epsilon = 0.001

print(normalSquareRoot(x, epsilon))
print(square_root_bisection(x, epsilon))
print(square_root_newton(x, epsilon))
