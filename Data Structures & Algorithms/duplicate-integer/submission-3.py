class Solution:
   def hasDuplicate(self, nums: list[int]) -> bool:
      dup = set()

      for num in nums:
         if num in dup:
            print("True")
            return True
         dup.add(num)
      print("False")
      return False

solution = Solution()

result = solution.hasDuplicate(nums=[1,2,3])