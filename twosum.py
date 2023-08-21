def twoSum(self, nums: List[int], target: int) -> List[int]: # the actual function itself
        
        for x in range(len(nums)): # main loop to loop through the list (0-the length of the input)
          
            for z in range(x + 1, len(nums)): # secondary loop to loop through the index after x
              
                    if nums[z] == target - nums[x]: # checks whether or not z is the difference between the target and nums
                      
                        return [x, z] # if it is, boom return the indicies that do so

# side note: ik this is basically the brute fore code on the solutions tab
# i basically just started leetcode give me a break >=( (at least i get the code lol)
