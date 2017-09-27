#https://www.hackerrank.com/contests/projecteuler/challenges/euler093/

import itertools

def closeEnough(val):
    EPSILON = 0.0001
    mod1 = val % 1
    return mod1 < EPSILON or mod1 > (1 - EPSILON)


def applyOperations(vals, vals_found):
    num_of_operations = len(vals) - 1
    if num_of_operations == 0 and closeEnough(vals[0]) and vals[0] >= 1:
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
                applyOperations(arr, vals_found)


def div(index, arr):
    if index >= len(arr):
        raise IndexError
    if arr[index + 1] == 0:
        raise ZeroDivisionError
    return arr[:index] + [arr[index] / arr[index + 1]] + arr[index+2:]

def mul(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] * arr[index + 1]] + arr[index+2:]

def add(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] + arr[index + 1]] + arr[index+2:]

def sub(index, arr):
    if index >= len(arr):
        raise IndexError
    return arr[:index] + [arr[index] - arr[index + 1]] + arr[index+2:]

def main():
    n = int(input())
    # input them as floats to call is_integer later
    vals = [float(i) for i in input().split()]
    vals = vals[:n]
    vals_found = set()
    # removes all duplicate tuples
    permutates = set(itertools.permutations(vals))
    for permutation in permutates:
        l_perm = list(permutation)
        applyOperations(l_perm, vals_found)
    vals_found_list = sorted(list(vals_found))
    index = 0
    cnt = 1
    if not vals_found_list:
        return 0
    while vals_found_list[index] == cnt:
        index += 1
        cnt += 1
        if index >= len(vals_found_list):
            break
    return cnt - 1

if __name__ == "__main__":
    print(main())