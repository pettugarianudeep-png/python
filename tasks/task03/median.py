# 1 Find median of Find median of [10,20,30,40,50] 
# import numpy as np
# values =   [10,20,30,40,50] 
# numbers = np.median(values)
# print("the midddle value:",numbers)

# 2 Find median of odd numbers array 

# def find_median(arr):
#     arr.sort()
#     middle = len(arr)//2
#     return arr[middle]

# nums = [10,20,30,40,50]

# result = find_median(nums)
# print(result)

# 3 Find median of even numbers array 

# def find_median(arr):
#     arr.sort()
#     middle1 = len(arr)//2 
#     middle2 = len(arr)//2 -1
#     return (arr[middle1] + arr[middle2]) / 2

# nums = [10,20,30,40]
# result = find_median(nums)
# print(result)

# 4Write function for median 
# def find_median(arr):
#     arr.sort()
#     n = len(arr)

#     if n% 2 ==1:
#         return arr[n//2]
    
#     else:
#         return(arr[n//2]+arr[(n//2)]-1)/2
    
# num1  = [10,20,30,40,50]
# num2  = [10,20,30,40]

# print("Median(odd):",find_median(num1))
# print("Median(even):",find_median(num2))

# 5 Compare mean and median in same array
# def compare_mean_median(arr):
#      mean = sum(arr)/ len(arr)
#      arr.sort()
#      n = len(arr)

#      if n% 2 == 1:
#          median = arr[n//2]
#      else:
#          median = (arr[n//2]+arr[(n//2)-1]) /2

#          print("Mean:",mean)
#          print("Median:",median)

#      if mean> median:
#          print("Mean is greater than Median")
#      elif median > mean:
#          print("Median is greater than Median")
#      else :
#          print("Mean and Median are equal")

# nums = [10,20,30,40,100]

# compare_mean_median(nums)



    

