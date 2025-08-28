from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = int(0)
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    for k in range(j, len(nums)):
            nums[k]=0    
    print(nums)        

moveZeroes([0, 1, 0, 3, 12])
        