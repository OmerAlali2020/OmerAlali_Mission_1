import sys

# Question 1:
# Code before fixing
print('Pre - Fix code:', (abs(3.0*(4.0/3.0-1)-1)))

# Code after fixing
print('Fix code:', (abs(3.0*(4.0/3.0-1)-1)-sys.float_info.epsilon))

# Question 3:
# Find the machine precision by function:
print('The machine precision is (func):', sys.float_info.epsilon)

# Find the machine precision by algorithm:
precision = 1

while 1.0 + (precision/2) > 1.0:
    precision = precision / 2
print('The machine precision is (alg):', precision)

# Both results is the same
