from random import randrange
from math import gcd

print('Hello. This is a Miller-Rabin test for primality. It have O(k*log^3(n)) running time complexity, where k is a number of rounds and n is a number to test.')
print('Enter an integer to be tested for primality which is greater than 2:')
number = int(input())
while(number < 2):
    print('Number is less than 2. Enter an integer to be tested for primality which is greater than 1:')
    number = int(input())

print('Enter round count:')
iterations = int(input())
while(iterations <= 0):
    print('Round count is less than 0. Please enter round count greater than 0:')
    iterations = int(input())


def miller_rabin_test(n, k):
    '''
    :param n: number to be tested
    :param k: number of iterations, 
    :return: True if number is probably prime, False otherwise
    '''
    d = n - 1
    s = 0
    while(d % 2 == 0):
        s += 1
        d = d // 2

    for tries in range(k):
        # choose witness to test with
        randomnum = randrange(1, n - 1)

        # test for gcd, if -1 then it is composite number
        if(gcd(randomnum, n) != 1):
            # number is composite
            return False
        
        x = pow(randomnum, d, n)
        # if x is 1 then it is probably prime number, if not check for second factor
        if(x != 1):
            i = 0

            # second factor check
            while(x != n - 1):
                # if all witnesses checked then it is a composite number
                if(i == s - 1):
                    # number is composite
                    return False
                else:
                    i = i + 1
                    x = pow(x, 2, n)

    # number is probably prime
    return True

test = miller_rabin_test(number, iterations)
if(test == True):
    print('Number ', number, ' is probably prime with ', '1 - 4^(-' + str(iterations) + ')' ,'probability to be true.')
else:
    print('Number ', number, ' is a composite number.')
