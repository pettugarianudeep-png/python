#1 Sort [45,12,78,9,34] 
# import numpy as np
# data = np.array([45,12,78,9,34])
# print(np.sort(data))

#  2Sort marks in ascending order
# import numpy as np
# ascending_order = np.array([80,35,45,65,25])
# print(np.sort(ascending_order))

# 3 Sort salary data 
# import numpy as np
# salaries = np.array([25000,18000,32000,15000])
# print(np.sort(salaries))


#  4 Write function to sort array 

# def sort_array(arr):
#     return sorted(arr)

# numbers = [45,5,65,60,30]
# print(sort_array(numbers))

# manual method code

# def sort_array(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#             return arr
        
# nums = [12,5,100,15,20]
# result = sort_array(nums)
# print(result)

# 5 Sort and print highest value separately 

# import numpy as np
# def sort_array(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                arr[i],arr[j]= arr[j],arr[i]
#             return arr


        
# nums = [45,12,78,9,34]
# result = sort_array(nums)
# print("sorted array:",result)
# print("Highest value:",result[-1])