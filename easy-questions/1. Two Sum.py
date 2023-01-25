def twoSum(nums, target):
    answer_array=[];
    for index,value in enumerate(nums):
        while index < len(nums):
            if (value + nums[index] == target and nums.index(value) != index):
                answer_array.append(nums.index(value))
                answer_array.append(index)
            index+=1
        if(answer_array):break
    return answer_array
        
numarray = [3,2,4]
target = 6
    
value = twoSum(numarray, target)
print(value)