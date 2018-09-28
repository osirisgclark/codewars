# #7 kyu Money, Money, Money

# Description:
# Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' this sum has to be kept in the bank in order for this sum of money to amount to 'D'.
# The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, and the new sum is re-invested yearly after paying tax 'T'
# Note that the principal is not taxed but only the year's accrued interest

# Example:
#   Let P be the Principal = 1000.00      
#   Let I be the Interest Rate = 0.05      
#   Let T be the Tax Rate = 0.18      
#   Let D be the Desired Sum = 1100.00


# After 1st Year -->
#   P = 1041.00
# After 2nd Year -->
#   P = 1083.86
# After 3rd Year -->
#   P = 1128.30
# Thus Mr. Scrooge has to wait for 3 years for the initial pricipal to ammount to the desired sum.
# Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

# Assumptions : 
# Assume that Desired Principal 'D' is always greater than the initial principal, however it is best to take into consideration that if the Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.

def calculate_years(principal, interest, tax, desired):
    y = 0
    sum = principal
    while sum < desired:
    	y += 1
    	yearly_interest = sum * interest
    	yearly_interest -= yearly_interest * tax
    	sum += yearly_interest
    return y

print(calculate_years(1000,0.05,0.18,1000))
print(calculate_years(1000,0.01625,0.18,1200))
print(calculate_years(1000, 0.05, 0.18, 1100))


#Otro mio:
# def calculate_years(principal, interest, tax, desired):
#     y = 0
#     while desired > principal:
#         y += 1
#         principal = principal*(1+interest)-principal*interest*tax
#     return y


# Best:
# def calculate_years(principal, interest, tax, desired):
#     years = 0
    
#     while principal < desired:
#         principal += (interest * principal) * (1 - tax)
#         years += 1
     
#     return years

# from math import ceil, log

# def calculate_years(principal, interest, tax, desired):
#     return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))