class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
       
        window = set()
        for right in range(len(nums)):

            if right > k:
                window.remove(nums[right-k-1])

            if nums[right] in window :
                return True

            window.add(nums[right])

        return False