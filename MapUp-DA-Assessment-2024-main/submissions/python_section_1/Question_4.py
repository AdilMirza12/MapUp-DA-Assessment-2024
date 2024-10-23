# Question 4: Generate Unique Permutations

def unique_permutations(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    nums.sort()
    result = []
    used = [False] * len(nums) 
    backtrack([], used)
    return result
input_list = [1, 1, 2]
output = unique_permutations(input_list)
for perm in output:
    print(perm)