# 1

nums = [8, 800, 5, 5, 5, 3, 5, 3, 5]
numb = list()
# a)
print(set(nums))
# б)
dig1 = ''
dig2 = ''
for i in range(0, len(nums)):
    co = 0
    for j in range(0, len(nums)):
        if nums[i] == nums[j] and nums[i] != dig1 and nums[i] != dig2:
            co += 1
            if co == 2:
                dig1 = nums[i]
                numb.append(nums[j])
    if co == 1:
        numb.append(nums[i])
    dig2 = nums[i - 1]
print(numb)