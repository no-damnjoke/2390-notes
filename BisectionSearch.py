#Finding Root x

import timeit
start = timeit.default_timer()

x = 1.21
epsilon = 0.001
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)

if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)

print(f'Total configuration execution time: {(timeit.default_timer() - start):.4f}s.', flush=True)