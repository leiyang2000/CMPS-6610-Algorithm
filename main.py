"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

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


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, False)
    if n == 1:
        is_key = (mylist[0] == key)
        return Result(int(is_key), int(is_key), int(is_key), is_key)

    mid = n // 2

    # Recursive calls
    result_left = longest_run_recursive(mylist[:mid], key)
    result_right = longest_run_recursive(mylist[mid:], key)

    # Calculate merged_mid, which is the longest sequence crossing the mid-point
    merged_mid = 0
    if mylist[mid-1] == key and mylist[mid] == key:
        merged_mid = result_left.right_size + result_right.left_size

    # Calculate longest_size for the combined list
    longest_size = max(result_left.longest_size, result_right.longest_size, merged_mid)

    # Calculate prefix and suffix for the combined list
    if result_left.is_entire_range and mylist[mid] == key:
        prefix_size = result_left.left_size + result_right.left_size
    else:
        prefix_size = result_left.left_size

    if result_right.is_entire_range and mylist[mid - 1] == key:
        suffix_size = result_right.right_size + result_left.right_size
    else:
        suffix_size = result_right.right_size

    # Determine if the entire range is filled with the key
    is_entire_range = result_left.is_entire_range and result_right.is_entire_range and mylist[mid-1] == key and mylist[mid] == key

    return Result(prefix_size, suffix_size, longest_size, is_entire_range)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12).longest_size == 3 




test_longest_run()