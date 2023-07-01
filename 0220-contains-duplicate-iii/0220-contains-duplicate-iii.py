from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if len(nums) == 0 or indexDiff <= 0:
            return False

        window = SortedList()

        for i in range(len(nums)):
            left = window.bisect_left(nums[i] - valueDiff)
            right = window.bisect_right(nums[i] + valueDiff)

            if left != right:
                print(left,right,nums[i])
                print(window)
                return True

            window.add(nums[i])

            if i >= indexDiff:
                window.remove(nums[i - indexDiff])
        print(window)
        return False
