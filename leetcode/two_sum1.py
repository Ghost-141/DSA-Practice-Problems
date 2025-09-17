#Two Sum Problem No.1 from LeetCode
# Using Hashmap with 
def get_pos(nums:list, target: int) -> list:
    seen = {}
    for key, value in enumerate(nums):
        x = target - value
        if x in seen:
            return [seen[x], key]
        seen[value] = key
nums = [2,7,11,15]
print(get_pos(nums=nums, target=9))