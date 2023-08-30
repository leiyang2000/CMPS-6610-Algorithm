def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb


def longest_run(myarray, key):
    max_run = 0
    current_run = 0
    for element in myarray:
        if element == key:
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0
    return max(max_run, current_run)



def longest_run_recursive(myarray, key):
    if len(myarray) == 0:
        return 0, 0, 0
    if len(myarray) == 1:
        return (1 if myarray[0] == key else 0, 1 if myarray[0] == key else 0, 1 if myarray[0] == key else 0)
    
    mid = len(myarray) // 2
    left_max, left_prefix, left_suffix = longest_run_recursive(myarray[:mid], key)
    right_max, right_prefix, right_suffix = longest_run_recursive(myarray[mid:], key)
    merged_mid = 0
    if myarray[mid-1] == myarray[mid]:
        merged_mid = left_suffix + right_prefix 
    max_run = max(left_max, right_max, merged_mid)
    prefix_run = left_prefix + right_prefix if left_prefix == mid and myarray[mid-1] == myarray[mid] else left_prefix
    suffix_run = right_suffix + left_suffix if right_suffix == len(myarray) - mid and myarray[mid-1] == myarray[mid] else right_suffix
    
    return max_run, prefix_run, suffix_run

if __name__ == "__main__":
    array = [2,12,12,8,12,12,12,0,12,1]
    max_run, _, _ = longest_run_recursive(array, 12)
    print(max_run)

    b = longest_run(array, 12)
    print(b)