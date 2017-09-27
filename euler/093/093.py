import itertools
# Doesn't pass all tests
# Brute force attempt, passes all timeouts

def applyOperations(val, vals_found):
    num_of_operations = len(val) - 1
    if num_of_operations == 0 and val[0].is_integer() and val[0] >= 1:
        vals_found.add(int(val[0]))
        return
    for i in range(num_of_operations):
        x = [0 for i in range(4)]
        x[0] = mul(i, val)
        x[1] = add(i, val)
        x[2] = sub(i, val)
        try:
            x[3] = div(i, val)
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
    _ = input()
    val = [float(i) for i in input().split()]
    vals_found = set()
    # removes all duplicate tuples
    permutates = set(itertools.permutations(val))
    for permutation in permutates:
        l_perm = list(permutation)
        applyOperations(l_perm, vals_found)
    vals_found_list = sorted(list(vals_found))
    index = 0
    cnt = 1
    while vals_found_list[index] == cnt:
        index += 1
        cnt += 1
        if index >= len(vals_found_list):
            break
    return cnt - 1

if __name__ == "__main__":
    print(main())