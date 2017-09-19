#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

import sys
import math

def create_palindromes(val):
    """
    mirrors val and returns that palindrome
    """
    strVal = str(val)
    strVal += strVal[::-1]
    return int(strVal)

def is_3_digit_prod(num):
    """
    returns True if it is a product of 2 3-digit numbers
    otherwise returns False
    uses maxVal to "pivot" around the square root of the number
    """
    maxVal = math.floor(math.sqrt(num)) + 1
    for factor1 in range(101, maxVal):
        factor2 = num / factor1
        if factor2 >= 100 and factor2 < 1000 and (factor2).is_integer():
            return True
    return False

def gen_6_digit_palindromes():
    """creates 6 digit palindromes"""
    for i in range(101, 1000):
        yield create_palindromes(i)

def search(n, palindromes):
    """
    returns the index number of n in palindromes
    the value of palindromes[index] < n
    log(n) search method
    """
    left = 0
    right = len(palindromes) - 1
    mid = right//2
    while (mid != left):
        if palindromes[mid] >= n:
            right = mid
            mid = (left + right)//2
        if palindromes[mid] < n:
            left = mid
            mid = (left + right)//2
    if palindromes[mid] >= n:
        return mid - 1
    return mid

def main():
    palindromes = list(pali for pali in gen_6_digit_palindromes() if is_3_digit_prod(pali))
    tests = int(input().strip()) # number of tests to run
    for test in range(tests):
        n = int(input().strip()) # test value
        pali_max_n = search(n, palindromes)
        print(palindromes[pali_max_n])

if __name__ == '__main__':
    main()