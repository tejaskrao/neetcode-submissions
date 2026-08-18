class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charset=set()
        l=0
        res=0
        
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[right])
            res=max(res,right-l+1)

        return res
        

        
                
