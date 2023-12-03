def my_square_root(x, epsilon):
    """
    Assumes x, epsilon floats
    x >= 0
    epsilon > 0 
    Returns result such that x-epsilon <= result*result <= x+epsilon
    """
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0

    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:
            low = ans 
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of', x)
    return ans

def test_my_square_root():
    
    print(my_square_root(x=0.0, epsilon=0.0001))
    print('-------------------------------------------------------')
    print(my_square_root(x=25.0, epsilon=0.0001))
    print('-------------------------------------------------------')
    print(my_square_root(x=0.5, epsilon=0.0001))
    print('-------------------------------------------------------')
    print(my_square_root(x=2.0, epsilon=0.0001))
    print('-------------------------------------------------------')
    print(my_square_root(x=2.0, epsilon=1.0/2.0**32.0))
    print('-------------------------------------------------------')
    print(my_square_root(x=1.0/2.0**16.0, epsilon=1.0/2.0**32.0))
    print('-------------------------------------------------------')
    print(my_square_root(x=2.0**16.0, epsilon=1.0/2.0**32.0))
    print('-------------------------------------------------------')
    print(my_square_root(x=2.0**16.0, epsilon=2.0**16.0))

def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of vect1[i]/vect2[i]"""
    ratios = []
    for index in range(len(vect1)):
        try: 
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError: 
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios