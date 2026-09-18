from typing import List


def can_reach_last_index(nums: List[int]) -> bool:
    """
    Determines whether the last index can be reached from index 0.

    :param nums: List of non-negative integers representing maximum jump lengths.
    :return: True if the last index can be reached, False otherwise.
    """
    if not nums:
        return False

    if len(nums) == 1:
        return True

    max_reach = 0
    target_index = len(nums) - 1

    for i, jump in enumerate(nums):
        # If current index is unreachable from any previous jump
        if i > max_reach:
            return False

        # Update maximum reachable index
        max_reach = max(max_reach, i + jump)

        # Early termination if target is reached or passed
        if max_reach >= target_index:
            return True

    return max_reach >= target_index


if __name__ == "__main__":
    test_cases = [
        {"nums": [2, 3, 1, 1, 4], "expected": True, "name": "Example 1"},
        {"nums": [3, 2, 1, 0, 4], "expected": False, "name": "Example 2"},
        {"nums": [0], "expected": True, "name": "Single element [0]"},
        {"nums": [5], "expected": True, "name": "Single element [5]"},
        {"nums": [2, 0, 0], "expected": True, "name": "Jump over zero"},
        {"nums": [0, 2, 3], "expected": False, "name": "Initial zero block"},
        {"nums": [10, 0, 0, 0, 0], "expected": True, "name": "Big jump at start"},
        {"nums": [1, 1, 1, 1], "expected": True, "name": "Consecutive single steps"},
    ]

    print("=== Running Question 1 (Python) Tests ===")
    passed = 0
    for tc in test_cases:
        res = can_reach_last_index(tc["nums"])
        status = res == tc["expected"]
        if status:
            passed += 1
        print(f"[{'PASS' if status else 'FAIL'}] {tc['name']}: nums={tc['nums']} => Result={res}, Expected={tc['expected']}")

    print(f"\nResult: {passed}/{len(test_cases)} tests passed.")