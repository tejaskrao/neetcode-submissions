class Solution:
    def isAnagram(self, s: str, t: str):

        len1 = len(s)
        len2 = len(t)
        counts1= {}
        counts2= {}
        if len1==len2:
            for char in s:
                if char in counts1:
                    counts1[char]+=1
                else:
                    counts1[char]=1

            
            for char in t:
                if char in counts2:
                    counts2[char]+=1
                else:
                    counts2[char]=1
        else:
            return False


        if counts1==counts2:
            return True
        else: 
            return False

            



        