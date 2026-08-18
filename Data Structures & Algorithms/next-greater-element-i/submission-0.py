class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack =[]
        nge={}

        for num in reversed (nums2):
            while stack and stack[-1] <=num:
                stack.pop()
            if stack:
                nge[num] = stack[-1]
            else:
                nge[num] = -1
            
            stack.append(num)

        return [nge[num] for num in nums1]
