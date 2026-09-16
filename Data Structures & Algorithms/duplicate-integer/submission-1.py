class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = []
        for x in nums:
            if x in hashmap:
                print(hashmap)
                return True
            hashmap.append(x)
        return False


                

