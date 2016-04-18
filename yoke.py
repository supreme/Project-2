#  Stephen Andrews
matrix = [[9, 2, 7, 8],
		  [6, 4, 3, 7],
		  [5, 8, 1, 8],
		  [7, 6, 9, 4]]

def greedy():
	# By default assume that this is the most efficient way to crack the messages
	# The index in the array represents the cryptographer
	assignment = [0, 0, 0, 0]
	for p_index in range(0, len(matrix)):
		person = matrix[p_index]
		lowest = 999
		for c_index in range(0, len(person)):
			cost = person[c_index]
			if (cost < lowest):
				lowest = cost
				assignment[p_index] = (c_index + 1) # +1 because array is zero based
		lowest = 999
	print(assignment)

greedy()

