def sequence_slayer(num):
	if(num == 0):
		return 1
	if(num == 1):
		return 2
	return ((num**2)*sequence_slayer(num-1))-sequence_slayer(num-2)
