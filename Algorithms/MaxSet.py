"""
Algorithm to find the greatest sum of non-consecutive integers given an array of integers.
Uses Dynamic Programming to find the optimal value and tracing to find the integers that
formed the optimal value.
"""



def optimal_solution(nums: list, cache: list):
    """
    Helper function utilized with max_set(), uses backwards tracing to find
    an array of integers that formed the optimal solution.
    Time Complexity O(n). Space Complexity O(log(n)).
    """
    # Starting from the max sum/optimal solution found previously.
    maxNum = cache[len(cache) - 1]
    n = len(nums)
    # An array that holds the integers that formed the optimal solution.
    numList = []
    # Iterate backwards in nums.
    for i in range(n-1, -1, -1):
        # Temporary value to see if the current element was used
        # to find the max sum by checking the cache.
        val = maxNum - nums[i]
        # Checking the cache to see if the temp value was a sub problem.
        if val in cache or val == 0:
            numList.append(nums[i])
            # Update maxNum variable to trace backwards farther.
            maxNum = val

    # Returns a list of integers that formed the optimal solution.
    return numList


def max_set(nums: list[int]):
    """
    Utilizes Dynamic Programming to find an optimal solution and an array
    of integers that formed the optimal solution.
    Time Complexity θ(n). Space Complexity ~O(1) if nums is < 3.
    Otherwise Space Complexity is θ(n) when n >= 3 to form a cache.
    """
    n = len(nums)
    # Invalid input.
    if n < 0:
        return
    # Base case 1 where the num array is empty and 0 is the optimal solution by default.
    if n == 0:
        return [0]
    # Base Case 2, where the only number is the optimal solution.
    if n == 1:
        return nums
    # Base Case 3, where the optimal solution is determined between the only two numbers.
    if n == 2:
        return [nums[1]] if nums[1] > nums[0] else [nums[0]]

    # A cache to store the sub problems.
    cache = [0 for x in range(n)]
    # Assigning the first two sub problem solutions by default.
    cache[0] = nums[0]
    cache[1] = nums[1] if nums[1] > nums[0] else nums[0]

    # Start at the third element in nums array since the first two elements have been solved.
    for k in range(2, n):
        # Find max between current number in the array and the current number
        # plus the previous non-adjacent number.
        cache[k] = max(cache[k-1], cache[k-2] + nums[k])
        cache[k] = max(nums[k], cache[k])

    # Returns the last index in the cache which should hold the solution
    # and returns an array of integers that formed the optimal solution.
    numList = optimal_solution(nums, cache)
    numList.reverse()
    return cache[k], numList


arr1 = [7,2,5,8,6]
arr2 = [-1, -1, 0]
arr3 =  [-1, -1, -10, -34]
arr4 = [2, 1, 6, 9]
arr5 = []
arr6 = [-21, -2,-5,-1,-1]
arr7 = [-1]
arr8 = [3,2]
print(max_set(arr1))