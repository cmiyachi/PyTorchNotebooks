# Python program for calculating Mean Absolute Error

# consider a list of integers for actual
actual = [2, 3, 5, 5, 9]

# consider a list of integers for actual
calculated = [3, 3, 8, 7, 6]

n = 5
sum = 0

# for loop for iteration
for i in range(n):
	sum += abs(actual[i] - calculated[i])

error = sum/n

# display
print("Mean absolute error : " + str(error))
