# Primality tests
Hello, here you can find Miller-Rabin and Solovay-Strassen primality tests python 3 implementations.

# Guide

- To test the number with the Miller-Rabin probability test you should execute it by using the Python3 interpreter using **"python3 Miller_Rabin_test.py”** command and follow the instructions on the terminal.
- To test the number with the Solovay-Strassen probability test you should execute it by using the Python3 interpreter using **“python3 Solovay_Strassen_test.py”** command and follow the instructions on the terminal.

# Application tested on
Application tested on Windows 10 with Python 3.11.0. Python 3 dependencies are random and math packages.

# Miller-Rabin primality test

## Running time complexity
Miller-Rabin running time complexity for this implementation is O(k*log^3(n)), where k is the number of rounds and n is the number to test.

## Probability of an integer to be a prime number
The probability of an integer is a prime number when the test says so is 1 - 4^(-k), where k is the number of rounds.

## Algorithm pseudocode primality test
```
Input #1: n > 2, an odd integer to be tested for primality
Input #2: k, the number of rounds of testing to perform
Output: “composite” if n is found to be composite, “probably prime” otherwise

let s > 0 and d odd > 0 such that n − 1 = 2^(s)*d  # by factoring out powers of 2 from n − 1
repeat k times:
    a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
    x ← a^d mod n
    if x != 1:
        i ← 0
        while x != n - 1
            if i == s - 1:
                return "composite"
            else:
                i ← i + 1
                x ← x^2 mod ny
return “probably prime”
```

# Solovay-Strassen primality test

## Running time complexity
Solovay-Strassen running time complexity for this implementation is O(k*log^3(n)), where k is a number of rounds and n is a number to test.

## Probability of an integer to be a prime number
The probability of an integer is a prime number when the test says so is 1 - 2^(-k), where k is the number of rounds.

## Algorithm pseudocode for Solovay-Strassen
```
inputs: n > 1, a value to test for primality
        k, a parameter that determines the accuracy of the test
output: composite if n is composite, otherwise probably prime

repeat k times:
    choose a randomly in the range [2,n − 1]
    x <- (a/n) get the jacobian number of a and n
    if x = 0 or a^((n-1)/2) !≡ x (mod n) then 
        return composite
return probably prime
```

## Algorithm for Jacobi number
1. Reduce the "numerator" modulo the "denominator" using rule 2.
2. Extract any even "numerator" using rule 9.
3. If the "numerator" is 1, rules 3 and 4 give a result of 1. If the "numerator" and "denominator" are not coprime, rule 3 gives a result of 0.
4. Otherwise, the "numerator" and "denominator" are now odd positive coprime integers, so we can flip the symbol using rule 6, then return to step 1.

Rules can be checked [here](https://en.wikipedia.org/wiki/Jacobi_symbol#Properties)

# Sources
Pseudocodes were partially taken from:
1. https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test 
2. https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test#Algorithm_and_running_time.

The algorithm for Jacobi number was taken from 
1. https://en.wikipedia.org/wiki/Jacobi_symbol#Calculating_the_Jacobi_symbol

