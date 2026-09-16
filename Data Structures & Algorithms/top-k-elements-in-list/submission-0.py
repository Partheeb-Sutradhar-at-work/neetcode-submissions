class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        final_list = []
        for x in nums:
            hashmap[x] = 1 + hashmap.get(x,0)
        sorted_map =sorted(hashmap, key=hashmap.get,reverse=True)
        
        return(sorted_map[0:k])
        

            

            
        
            

        