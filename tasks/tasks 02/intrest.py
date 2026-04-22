# # Write a function with two arguments: principal and rate, and return simple interest.

# def simple_intrest(p,r,t=1):
#     return(p*r*t/100)

# principal = int(input("Enter the Amount"))
# rate  = int(input("Enter the rate"))

# print(f"The simple interest of {principal} and {rate}%  of interst for 1 year is{simple_intrest(principal,rate)} ruppees")


# Write a function that accepts student marks and returns grade (A/B/C/Fail).

# def student_marks(mark):
#     if mark>90:
#         return"Agrade"
#     elif mark > 75:
#        return"B grade"
#     elif mark>=35:
#         return"Cgrade"
#     else:
#         return"Failed  study again"

# num = int(input("Enter the marks:"))    
# print(student_marks(num))

#Write a function that takes a number and returns whether it is prime or not. 

# def is_prime(num):
#     if num <= 1:
#        return  False
    
#     for i in range(2,num):
#         if num % i == 0:
#             return False
        
#     return True

# print(is_prime(8))

