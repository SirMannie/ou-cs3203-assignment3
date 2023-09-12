
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

def rlist(numbers):



	return numbers[::-1]



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