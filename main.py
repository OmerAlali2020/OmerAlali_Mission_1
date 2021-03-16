import sys

# Question 1:
# Code before fixing
print('Pre - Fix code:', (abs(3.0*(4.0/3.0-1)-1)))

# Code after fixing
print('Fix code:', (abs(3.0*(4.0/3.0-1)-1)-sys.float_info.epsilon))

# Question 3:
# find the machine precision
print('The machine precision is:', sys.float_info.epsilon)
