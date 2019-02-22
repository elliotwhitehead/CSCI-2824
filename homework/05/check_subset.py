def check_subset(A,B):
	if (len(A) and len(B)):
		found = True
		for x in A:
			if x not in B:
				found = False
		if found:
			return found
		found = True
		for y in B:
			if y not in A:
				found = False
		return found
	else:
		return True