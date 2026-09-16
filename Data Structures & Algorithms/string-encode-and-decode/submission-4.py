class Solution:

    def encode(self, strs: List[str]) -> str:
        list_encode = ""
        for i in strs:
            reversed_word = "".join(reversed(i))
            reversed_word += "++"
            list_encode += reversed_word
        return list_encode


    def decode(self, s: str) -> List[str]:
        decoding_list = s.split("++")
        new_list = []
        #print(decoding_list)
        for i in decoding_list:
            Fixed_word = "".join(reversed(i))
            new_list.append(Fixed_word)
            #print(new_list)
        new_list.pop()
        #print(new_list)
        return new_list
        
        


