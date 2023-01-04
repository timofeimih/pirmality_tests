from random import randint

print('Hello. This is a Solovay-Strasset probability test. It have O(k*log^3(n)) running time complexity, where k is a number of rounds .')

print('Enter an odd integer to be tested for primality:')
number = int(input())
while(number <= 1):
    print('N is less than 1. Enter an odd integer to be tested for primality which is greater than 1:')
    number = int(input())

print('Enter round count:')
iterations = int(input())
while(iterations <= 0):
    print('Round count is less than 0. Please enter round count greater than 0:')
    iterations = int(input())

def jacobi(n, k):
    '''
    :param n: number n > 0
    :param k: number k > 0, k % 2 == 1
    :return: -1, 0 or 1
    
    Steps visual representation can be seen at https://en.wikipedia.org/wiki/Jacobi_symbol#Properties
    '''

    # check if k is odd number and k greater than 0
    assert(k % 2 == 1 and 0 < k)

    # Step 1:  Reduce the "numerator" modulo the "denominator" using rule 2.
    n = n % k

    # let`s assume that it is Jacobi symbol
    t = 1

    # Step 3: If the "numerator" is 1, rules 3 and 4 give a result of 1. If the "numerator" and "denominator" are not coprime, rule 3 gives a result of 0.
    while n != 0:

        # Step 2: Extract any even "numerator" using rule 9.
        while n % 2 == 0:
            n = n / 2
            r = k % 8
            # if remainder is 3 or 5 then Jacobi number is -1
            if r == 3 or r == 5:
                t = -t

        # Step 4: Otherwise, the "numerator" and "denominator" are now odd positive coprime integers, so we can flip the symbol using rule 6, then return to step 1.
        # interchange n and k 
        n, k = k, n
        # if remainder of both is 3 then Jacobi number is -1
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        # set n to remainder of n % k
        n = n % k

    # if after computation k is 1 then Jacobi number is 1 else it is 0
    if k == 1:
        return t
    else:
        return 0



def solovay_strassen(n, k=1):
    '''
    :param n > 1: number to be tested
    :param k: number of iterations, 
    :return: True if number is probably prime, False otherwise
    '''
    # check if n < 3 or n is not even, if one is true then check if it is 2 then return true(prime number), otherwise return false(composite number)
    if n < 3 or not n % 2:
        return n == 2

    for tries in range(k):
        # select random int less than n and greater than 2
        randomint = randint(2, n - 1)
        # calculate Jacobi number
        jacobian = jacobi(randomint, n)
        # check if number is composite 
        if not jacobian or pow(randomint, (n - 1)//2, n) != jacobian % n:
            # number is composite
            return False
    # number is probably prime
    return True


test = solovay_strassen(number, iterations)
if(test == True):
    print('Number ', number, ' is probably prime with ', '1 - 2^(-' + str(iterations) + ')' ,'probability to be true.')
else:
    print('Number ', number, ' is a composite number.')

