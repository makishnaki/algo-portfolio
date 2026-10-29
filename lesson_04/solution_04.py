# первая задача
def min_boats(weights, limit):
    if not weights:
        return 0
    weights_sorted = sorted(weights)
    left = 0
    right = len(weights_sorted) - 1
    boats = 0
    while left <= right:
        if weights_sorted[left] + weights_sorted[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats

# вторая задача
def even_first(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
