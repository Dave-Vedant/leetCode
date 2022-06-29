def guessNumber(n):
    i = 1
    j = n
    while i<j:
        mid = (i+j) /2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            j = mid
        else:
            i = mid +1
    return i

# execution
# guess is api return random value

import random
def guess(n):
    x = random.randint(0,100)
    return x

answer = guessNumber(10)
print(answer)

    