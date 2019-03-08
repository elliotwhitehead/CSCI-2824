def first_D_digit_Fib(digits):
	fib_array = [1,1]
	for i in range(2,10000):
		fib_array.append(fib_array[i-1] + fib_array[i-2])

	for val in fib_array:
		current_digits = len(str(val))
		if(current_digits == digits):
			return val