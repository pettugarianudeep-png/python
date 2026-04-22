# 1 Create one program showing mean, sum, max, min 
# import numpy as np
# nums = [10,20,30,40,50] 
# elements = np.sum(nums), np.mean(nums) ,np.max(nums) ,np.min(nums)
# print("Sum:,"np.sum(nums))
# print("Mean:,"np.sum(nums))
# print("Max:,"np.sum(nums))
# print("Min:,"np.sum(nums))

# 2  Create one function for all statistics
import numpy as np
# def find_statistics(data):
#     arr = np.array(data)
#     Total = np.sum(arr)
#     average = np.mean(arr)
#     high = np.max(arr)
#     low = np.min(arr)
#     standard_d= np.std(arr)
#     varaince_d = np.var(arr)

#     print("the total of the data:",Total)
#     print("the average of the data:",average)
#     print("the highest of the data:",high)
#     print("the lowest of the data:",low)
#     print("the standard deviation of the data:",standard_d)
#     print("the varaince of the data:",varaince_d)

# print(find_statistics([2,3,4,5,6,7]))

# Input marks and show all statistics 
import numpy as np
# def all_statistics(user):
#     arr = np.array(user)
#     Total = np.sum(arr)
#     average = np.mean(arr)
#     high = np.max(arr)
#     low = np.min(arr)
#     standard_d= np.std(arr)
#     varaince_d = np.var(arr)

#     print("the total of the data:",Total)
#     print("the average of the data:",average)
#     print("the highest of the data:",high)
#     print("the lowest of the data:",low)
#     print("the standard deviation of the data:",standard_d)
#     print("the varaince of the data:",varaince_d)

# marks = [int(input(f"Enter marks you scored in 5 subs:{i+1} ")) for i in range(5)]
# print(all_statistics(marks))

 # 4 Compare two arrays statistics 

# student1 = ([1,3,5,7,11])
# student2 = ([2,4,6,8,10])

# marks1 = np.array(student1)
# marks2 = np.array(student2)

# print("The student 1 average is good than student2",np.average(marks1)>np.average(marks2))
# print("The student 1 has highest marks  good than student2",np.max(marks1)>np.max(marks2))
# print("The s1> s2 marks",np.min(marks1)<np.min(marks2))
# print("The more consisteient is s1 > s2",np.std(marks1)>np.std(marks2))






