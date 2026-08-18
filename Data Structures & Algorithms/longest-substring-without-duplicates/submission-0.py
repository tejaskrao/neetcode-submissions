class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charset=set()
        l=0
        res=0
        
        for visit in range(len(s)):
            while s[visit] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[visit])
            res=max(res,visit-l+1)

        return res
        

        
                
