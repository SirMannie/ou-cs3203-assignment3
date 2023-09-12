
def computeSum(numbers):
	
	total = 0

	for number in numbers:
		total += number
	return total


def computeProduct(numbers):

	total = 1
	
	for number in numbers:
		total *= number
	return total




def getUserInput():
	user_input = input("Enter the numbers")
	numbers = [float(num) for num in user_input.split()]
	return numbers


numbers = getUserInput()
sums = computeSum(numbers)
product = computeProduct(numbers)

print(f"The sum is: {sums}")
print(f"The product is: {product}")