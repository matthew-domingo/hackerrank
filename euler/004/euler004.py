#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

import sys
import math

def createPalindrome(val):
    strVal = str(val)
    strVal += strVal[::-1]
    return int(strVal)

def is3DigitProduct(num):
    # use maxVal to "pivot" around the square root of the number
    maxVal = math.floor(math.sqrt(num)) + 1
    for factor1 in range(100, maxVal):
        factor2 = num // factor1
        if factor2 >= 100 and factor2 < 1000 and num % factor1 == 0:
            return True
    return False

def genPalindromes():
    for i in range(101, 1000):
        pali = createPalindrome(i)
        if is3DigitProduct(pali):
            yield pali


def main():
    palindromes = list(genPalindromes())
    #
    numOfTests = int(input().strip())
    for _ in range(numOfTests):
        N = int(input().strip())
        maxPali = 0
        # could do a max(p for p in palindromes if p < n), but that doesn't have a break function
        # and palindromes is in order
        for p in palindromes:
            if p >= N:
                break
            if p > maxPali:
                maxPali = p
        print(maxPali)

if __name__ == '__main__':
    main()