class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = nums[0]
        prefix_arr = [nums[0]]

        suffix_product = nums[-1]
        suffix_arr = [nums[-1]]
        

        for i in range(1,len(nums)):
            prefix_arr.append(prefix_product)
            prefix_product *= nums[i]
            
           
        
        for i in range(len(nums) - 2,-1,-1):
            suffix_arr.append(suffix_product)
            suffix_product *= nums[i]
            
        print(prefix_arr)
        print(suffix_arr)

        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_arr[ -1 * (i + 1)])
            elif i != len(nums) -1 :
                pre = prefix_arr[i]
                suffix = suffix_arr[ -1 * (i + 1)]
                print("pre", pre, "suffix", suffix)
                result.append(pre*suffix)
            else:
                result.append(prefix_arr[i])

        return result



        
