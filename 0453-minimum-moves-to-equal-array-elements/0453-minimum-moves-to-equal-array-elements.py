class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum=min(nums)
        move=0
        for num in nums:
            move+=num-minimum
        return move