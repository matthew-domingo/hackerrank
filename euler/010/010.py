#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

import sys

def primeSieve(n = 100):
    """
    returns a list of primes <= n
    Simple prime sieve, not optimized for numbers > 1000000
    """
    sieveLen = n + 1
    primes = []
    nextPrimes = [True for _ in range(sieveLen)]
    nextPrimes[0] = False
    nextPrimes[1] = False
    for i, isPrime in enumerate(nextPrimes):
        if isPrime:
            # upon finding the next prime, mark all multiples of that prime False
            for ii, __ in enumerate(nextPrimes[2*i::i]):
                nextPrimes[(ii+2)*i] = False
            primes.append(i)
    return primes


def printArrToSums(sortedSummingArr, iteratingArr):
    """
    prints the sum primeSum of each element
    Important function to speed up a large numbers of tests
    Instead of iterating through the prime list with each test,
    it iterates through each test twice and the prime list only once
    """
    arrSorted = sorted(iteratingArr)
    dictOfShortening = dict()
    currPrimeIndex = 0
    runningSum = 0
    # this part goes through the sorted array adds the appropriate values to a dictionary
    for num in arrSorted:
        while sortedSummingArr[currPrimeIndex] <= num:
            runningSum += sortedSummingArr[currPrimeIndex]
            currPrimeIndex += 1
        dictOfShortening[num] = runningSum
    # printing in the same order as the input array
    for num in iteratingArr:
        print(dictOfShortening[num])

def main():
    primes = primeSieve(10**6)
    t = int(input().strip())
    arr = []
    for a0 in range(t):
        arr.append(int(input().strip()))
    printArrToSums(primes, arr)

if __name__ == '__main__':
    main()