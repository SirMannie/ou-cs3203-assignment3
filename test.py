
import app

test_cases_sum = [
	([1,2,3], 6),
	([1,2,3,4,5], 15),
	([4,5], 9)
]

test_cases_product = [
	([1,2,3], 6),
	([1,2,3,4,5], 120),
	([4,5], 20)
]

for test_value_sum, expected_result_sum in test_cases_sum: 
	actual_result_sum = app.computeSum(test_value_sum)
	if app.computeSum(test_value_sum) == expected_result_sum:
		print('Test passed for sum')
	else:
		print(f'Test failed for sum input {test_value_sum}: Expected {expected_result_sum}, but got {actual_result_sum}')

for test_value_product, expected_result_product in test_cases_product:
	actual_result_product = app.computeProduct(test_value_product)
	if app.computeProduct(test_value_product) == expected_result_product:
		print('Test passed for product')
	else:
		print(f'Test failed for product input {test_value_product}: Expected {expected_result_product}, but got {actual_result_product}')