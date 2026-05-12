def get_user_input() -> list[int]:
    print("=" * 60)
    print("  Longest Subarray with Equal 0s and 1s")
    print("  Algorithm: Divide & Conquer  [Recursive]")
    print("=" * 60)
    print("HOW TO USE:")
    print("  - Enter array elements separated by spaces.")
    print("  - Only 0 and 1 are allowed.")
    print("  - Example: 0 1 0 0 1 1 0")
    print("=" * 60)

    while True:
        user_input = input("\n  Please enter the binary array: ").strip()

        if not user_input:
            print("  [Error] Input is empty. Please enter some numbers.")
            continue

        try:
            nums = [int(x) for x in user_input.split()]

            if any(val not in (0, 1) for val in nums):
                print("  [Error] Array must contain ONLY 0s and 1s.")
                print("  Hint: Remove numbers like 2, 3 ... and try again.")
                continue

            print("  [OK] Input accepted!\n")
            return nums

        except ValueError:
            print("  [Error] Invalid format — letters or symbols detected.")
            print("  Hint: Use only 0s and 1s separated by spaces.")


def _count_zeros_ones(arr: list[int], i: int, j: int) -> tuple[int, int]:
    """Returns (zero_count, one_count) for arr[i..j]."""
    zeros = sum(1 for k in range(i, j + 1) if arr[k] == 0)
    ones  = (j - i + 1) - zeros
    return zeros, ones


def _combine_crossing(arr: list[int],
                      left: int, mid: int, right: int) -> tuple[int, int, int]:
    """
    Checks every subarray arr[i..j] that crosses the midpoint
    (i <= mid < j) and returns the longest one with equal 0s and 1s.

    Returns:
        tuple: (max_length, best_start, best_end)
    """
    max_len    = 0
    best_start = -1
    best_end   = -1

    for i in range(left, mid + 1):
        zeros = 0
        ones = 0

        for k in range(i, mid + 1):
            if arr[k] == 0:
                zeros += 1
            else:
                ones += 1

        for j in range(mid + 1, right + 1):
            if arr[j] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones:
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len
                    best_start = i
                    best_end = j

    return max_len, best_start, best_end


def _divide_and_conquer(arr: list[int],
                        left: int, right: int) -> tuple[int, int, int]:
    """
    Recursively divides the array into halves, solves each half,
    then merges by checking the crossing subarray.

    Returns:
        tuple: (max_length, best_start, best_end)
    """
    if left >= right:
        return 0, -1, -1

    mid = left + (right - left) // 2

    left_len,  left_s,  left_e  = _divide_and_conquer(arr, left,    mid)
    right_len, right_s, right_e = _divide_and_conquer(arr, mid + 1, right)

    # Find best crossing subarray
    cross_len, cross_s, cross_e = _combine_crossing(arr, left, mid, right)

    if left_len >= right_len and left_len >= cross_len:
        return left_len, left_s, left_e
    elif right_len >= left_len and right_len >= cross_len:
        return right_len, right_s, right_e
    else:
        return cross_len, cross_s, cross_e


def longest_subarray_recursive(nums: list[int]) -> tuple[int, int, int]:
    """
    Entry point for the Divide & Conquer algorithm.

    Parameters:
        nums (list[int]): Binary array of 0s and 1s.

    Returns:
        tuple: (max_length, start_index, end_index)
    """
    n = len(nums)
    if n < 2:
        return 0, -1, -1

    return _divide_and_conquer(nums, 0, n - 1)

#   MAIN EXECUTION
if __name__ == "__main__":
    arr = get_user_input()

    length, start, end = longest_subarray_recursive(arr)

    print("=" * 60)
    print("  RESULT")
    print("=" * 60)
    print(f"  Input Array            : {arr}")
    print(f"  Longest Subarray Length: {length}")

    if start != -1:
        print(f"  Subarray Indices       : [{start} .. {end}]")
        print(f"  Subarray               : {arr[start:end + 1]}")
    else:
        print("  No valid subarray found.")

    print("=" * 60)