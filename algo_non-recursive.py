def get_user_input() -> list[int]:
    print("=" * 60)
    print("  Longest Subarray with Equal 0s and 1s")
    print("  Algorithm: HashMap + Prefix Sum  [Non-Recursive]")
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


def longest_balanced_subarray(arr: list[int]) -> tuple[int, int, int]:
    """
    Finds the longest contiguous subarray with equal number of 0s and 1s.

    Approach — Prefix Sum + HashMap:
      • Replace every 0 with -1, then compute a running prefix sum.
      • If the same prefix sum appears at index i and later at index j,
        the subarray arr[i+1 .. j] has equal 0s and 1s.
      • Store the FIRST occurrence of each prefix sum in a dictionary.

    Parameters:
        arr (list[int]): Binary array of 0s and 1s.

    Returns:
        tuple: (max_length, start_index, end_index)
               start_index and end_index are -1 if no valid subarray found.
    """
    n = len(arr)
    max_length  = 0
    start_index = -1
    end_index   = -1

    prefix_sum = 0

    first_occurrence = {0: -1}

    for i in range(n):
        if arr[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in first_occurrence:
            current_length = i - first_occurrence[prefix_sum]

            if current_length > max_length:
                max_length  = current_length
                start_index = first_occurrence[prefix_sum] + 1
                end_index   = i
        else:
            first_occurrence[prefix_sum] = i

    return max_length, start_index, end_index

#   MAIN EXECUTION
if __name__ == "__main__":
    arr = get_user_input()

    length, start, end = longest_balanced_subarray(arr)

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