class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProdArray = []
        rightProdArray = [0] * len(nums)
        returnArray = []
        for i in range(len(nums)):
            if(i > 0):
                leftProdArray.append(nums[i] * leftProdArray[i-1])
            else:
                leftProdArray.append(nums[i])
        
        print(leftProdArray)
        for i in range(len(nums) -1, -1,-1):
            if(i < len(nums) -1):
                rightProdArray[i] = nums[i] * rightProdArray[i + 1]
            else:
                rightProdArray[i] = nums[i]
            
        print(rightProdArray)
        for i in range(len(nums)):
            if i == 0:
                returnArray.append(rightProdArray[i + 1])
            elif i == len(nums) -1 :
                returnArray.append(leftProdArray[i-1])
            else:
                returnArray.append(rightProdArray[i+1] * leftProdArray[i-1])
        return returnArray

