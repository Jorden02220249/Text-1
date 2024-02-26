#and operator- True if both true
# Example 1
x = 5
print(x > 3 and x < 10) #True

# Example 2
y = 12
print( y > 10 and y % 5 == 0) # False

#Or operator- True if one is true
# Example 1
x = 5
print(x < 3 or x > 10) #false

#Example 2
y = 12
print(y < 10 or y % 2 ==0) #true

# Not operator
#Example 1
x = 5
print(not(x > 3 and x < 10)) #false because the condition is true

#Example 2
y = 12
print(not(y > 10 and y % 5 ==0)) #True as condition is false