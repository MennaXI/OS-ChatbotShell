def divide(a, b):
    return a / b  # no zero check


def max_value(nums):
    max_num = nums[0]  # fails if list is empty
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num


print(divide(10, 0))
print(max_value([]))

