#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

import sys
import math

def create_palindromes(val):
    strVal = str(val)
    strVal += strVal[::-1]
    return int(strVal)

def is_3_digit_prod(num):
    # returns True if it is a product of 2 3-digit numbers
    # otherwise returns False
    # use maxVal to "pivot" around the square root of the number
    maxVal = math.floor(math.sqrt(num)) + 1
    for factor1 in range(101, maxVal):
        factor2 = num / factor1
        if factor2 >= 100 and factor2 < 1000 and (factor2).is_integer():
            return True
    return False

def gen_6_digit_palindromes():
    #creates 6 digit palindromes
    for i in range(101, 1000):
        yield create_palindromes(i)

def main():
    palindromes = list(pali for pali in gen_6_digit_palindromes() if is_3_digit_prod(pali))
    # number of tests to run
    tests = int(input().strip())
    for test in range(tests):
        # test value
        n = int(input().strip())
        pali_max = 0
        # could do max(p for p in palindromes if p < n),
        # but that doesn't have a break function
        # and palindromes is already sorted
        for p in palindromes:
            if p >= n:
                break
            if p > pali_max:
                pali_max = p
        print(pali_max)

if __name__ == '__main__':
    main()