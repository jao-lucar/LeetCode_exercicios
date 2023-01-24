# Descrição do exercicio
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.


def sumtwo(nums, target):
    index_index_auxiliar = 0
    index = []

    while len(index) != 2:
        for n in nums:
            if nums[index_index_auxiliar] + n == target:
                index.append(nums.index(nums[index_index_auxiliar]))
                index.append(nums.index(n))

        index_index_auxiliar += 1
        if (len(nums) - 1) < index_index_auxiliar:
            return False

    return index


x = sumtwo(nums=[5, 1, 2, 6, 5], target=6)
print(x)


