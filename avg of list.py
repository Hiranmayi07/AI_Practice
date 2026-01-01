def find_average(nums):
    total = 0
    for x in nums:
        total += x
    return total / len(nums)
nums = list(map(int, input("Enter numbers: ").split()))
avg = find_average(nums)
print("Average:", avg)
