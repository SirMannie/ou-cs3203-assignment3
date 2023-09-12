
import app

test_cases = [
	([1,2,3], 6),
	([1,2,3,4,5], 15),
	([4,5], 9)
]

for test_value, expected_result in test_cases: 
	actual_result = app.computeSum(test_value)
	if app.computeSum(test_value) == expected_result:
		print('Test passed')
	else:
		print(f'Test failed for input {test_value}: Expected {expected_result}, but got {actual_result}')