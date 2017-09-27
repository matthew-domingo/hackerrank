#https://www.hackerrank.com/contests/projecteuler/challenges/euler093/

import itertools

"""
if val is within EPSILON of an integer, it returns true
"""
def close_enough(val, EPSILON = 0.0001):
    mod1 = val % 1
    return mod1 < EPSILON or mod1 > (1 - EPSILON)

"""
goes through vals (list) and applies +,-,*,/ reducing it until it's only 1 element
adds all the integer values >= 1 to vals_found
NOTE: This only works if the vals are numbers but not saved as integers
ex: [float(val) for val in vals] instead of [int(val) for val in vals]
"""
def apply_arithmetic_expressions(vals, vals_found):
    #TODO: find some way to decrease the number of operations
    num_of_operations = len(vals) - 1
    if num_of_operations == 0 and close_enough(vals[0]):
        vals_found.add(int(vals[0]))
        return
    for i in range(num_of_operations):
        x = [0 for i in range(4)]
        x[0] = mul(i, vals)
        x[1] = add(i, vals)
        x[2] = sub(i, vals)
        try:
            x[3] = div(i, vals)
        except ZeroDivisionError:
            x.pop()
        if num_of_operations > 0:
            for arr in x:
                apply_arithmetic_expressions(arr, vals_found)

"""
reduces an array by 1, divides the index by index + 1 and puts that in spot index
"""
def div(index, arr):
    if index >= len(arr):
        raise IndexError
    if arr[index + 1] == 0:
        raise ZeroDivisionError
    return arr[:index] + [arr[index] / arr[index + 1]] + arr[index+2:]

"""
reduces an array by 1, multiplies the index by index + 1 and puts that in spot index
"""
def mul(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] * arr[index + 1]] + arr[index+2:]

"""
reduces an array by 1, adds the index by index + 1 and puts that in spot index
"""
def add(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] + arr[index + 1]] + arr[index+2:]

"""
reduces an array by 1, subtracts the index by index + 1 and puts that in spot index
"""
def sub(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] - arr[index + 1]] + arr[index+2:]

"""
analyzes the result, finds the largest possible integer n such that from 1 to n, all integers are present
"""
def analyze_result(res):
    res = [val for val in res if val > 0]
    index = 0
    cnt = 1
    if not res:
        return 0
    while res[index] == cnt:
        index += 1
        cnt += 1
        if index >= len(res):
            break
    return cnt - 1

"""
returns a sorted list of all possible integers
created by all permutations of vals applied to the apply_arithmetic_expressions function
"""
def find_int_arithmetic_expressions(vals):
    vals_found = set()
    # removes all duplicate tuples
    permutates = set(itertools.permutations(vals))
    # fills vals_found
    for permutation in permutates:
        l_perm = list(permutation)
        apply_arithmetic_expressions(l_perm, vals_found)
    # Analysis of numbers found
    return sorted(list(vals_found))


def main():
    n = int(input())
    vals = [int(i) for i in input().split()]
    vals = vals[:n]
    res = find_int_arithmetic_expressions(vals)
    return(analyze_result(res))

if __name__ == "__main__":
    print(main())