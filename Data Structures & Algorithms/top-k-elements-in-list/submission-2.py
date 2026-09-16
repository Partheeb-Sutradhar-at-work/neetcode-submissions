class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        final_list = []
        for x in nums:
            hashmap[x] = 1 + hashmap.get(x,0)
        bucks =[[] for i in range(len(nums)+1)]
        for num,freq in hashmap.items():
            bucks[freq].append(num)
        for i in range(len(bucks)-1,0,-1):
            for n in bucks[i]:
                final_list.append(n)
                if len(final_list) == k:
                    return final_list



            
        

            

            
        
            

        