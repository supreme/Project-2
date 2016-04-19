#  Stephen Andrews
import itertools

matrix_1 = [[9, 2, 7, 8],
		  [6, 4, 3, 7],
		  [5, 8, 1, 8],
		  [7, 6, 9, 4]]

def exhaustive(matrix):
	# Create a list of possibile indicies in the n x m matrix
	index_range = list(range(len(matrix)))

	# Create a permutation of array indicies with itertools Python package
	permutation = (list(itertools.permutations(index_range)))

	min = -1
	assignment = []
	for j in range(len(permutation)):
		sum = 0
		for i in permutation[0]:
			sum = sum + matrix[i][permutation[j][i]]
		if sum < min or min == -1:
			min = sum
			assignment = permutation[j]
	return assignment

def greedy():
	# By default assume that this is the most efficient way to crack the messages
	# The index in the array represents the cryptographer
	assignment = [0] * 4 # FIXME
	for p_index in range(0, len(matrix_1)):
		person = matrix_1[p_index]
		lowest = -1
		for c_index in range(0, len(person)):
			cost = person[c_index]
			if (cost < lowest or lowest == -1) and not (c_index + 1 in assignment):
				lowest = cost
				assignment[p_index] = (c_index + 1) # +1 because array is zero based
		lowest = -1 # Reset

	# Compare any ties and find most efficient way to solve
	print(assignment)

print(exhaustive(matrix_1))

