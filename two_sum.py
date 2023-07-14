import random

nums = random.sample(range(1, 10), 5)
print("Array:", nums)
target = int(input(print("Enter target:")))

def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        comp = target - num
        if comp in hashmap:
            return [hashmap[comp], i]
        hashmap[num] = i
        print(comp,hashmap)
    return []  # No valid solution found

indices = twoSum(nums, target)

print("Indices of the two numbers:", indices)