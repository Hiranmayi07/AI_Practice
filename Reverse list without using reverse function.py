#Method1:Time complexity:O(n),space:O(n)
nums=list(map(int,input("Enter numbers:").split()))
num_rev=[]
n=len(nums)
for i in range(n):
    num_rev.append(nums[n-i-1])
print(num_rev)
#Method2:Time complexity:O(n),space:O(1)
nums = list(map(int, input("Enter numbers: ").split()))

l = 0
r = len(nums) - 1

while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

print(nums)

