import random

class Solution:
    def __init__(self, nums: 'List[int]'):
        self.orig = nums[:]
        self.shuffled = nums[:]

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffled = self.orig[:]
        return self.shuffled


    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        self.shuffled = self.orig[:]
        for i in range(0,len(self.shuffled)-1):
            j = random.randrange(i,len(self.shuffled))
            self.shuffled[i], self.shuffled[j] = self.shuffled[j], self.shuffled[i]

        return self.shuffled

# Your Solution object will be instantiated and called as such:

nums = [1,2,3,4,5,6]

obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

pass