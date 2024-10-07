class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {}
        
        nums[n] = True
        n_l = list(str(n))
        while n != 1:
            n_l = list(str(n))
            print(nums, n_l)
            result = 0
            for nl in n_l:
                result += (int(nl) ** 2)
            if nums.get(result) == True:
                # print(nums)
                # print(result, nums.get(result))
                return False
            else:
                nums[result] = True
                n = result
                # n_l = list(str(result))
        return True
        

        