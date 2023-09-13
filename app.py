
#computes the sum of an array of numbers
def computeSum(numbers):

	total = 0

	for number in numbers:
		total += number

	return total


#computes the product of an array of numbers
def computeProduct(numbers):

	total = 1

	for number in numbers:
		total *= number

	return total

#reverses the given array
def rlist(numbers):



	return numbers[::-1]


#takes user input
def getUserInput():
	user_input = input("Enter the numbers")
	numbers = [int(num) for num in user_input.split()]
	return numbers

def main():
	numbers = getUserInput()
	sums = computeSum(numbers)
	product = computeProduct(numbers)
	reverse = rlist(numbers)

	print(f"The sum is: {sums}")
	print(f"The product is: {product}")
	print(f"The array in reverse is: {reverse}")

main()