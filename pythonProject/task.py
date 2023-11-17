import os
#
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     print('pivoy: ', pivot)
#     print('less: ', less)
#     print('greater:', greater)
#     print('+++', less + [pivot] + greater)
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print('--------------------------------------------')
# print(quick_sort([3,4,1,2,9,7,0,26,9,6,4]))

def merge_sort(nums):
    if len(nums) > 1:
        x = len(nums)
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list_1 = [6,2,5,4,5,7,0]
merge_sort(list_1)
print(list_1)