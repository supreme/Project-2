Stephen Andrews
CS 2223 Project 2

This code was intended to be run with Python 3.x

Running instructions -
	- Navigate to directory containing fib.py
	- Execute 'python3 assig.py'

Navigating the menu -
	The menu was written with an effort to mimic the existing documentation
	style of terminal based programs. 

	Commands:
	example - Runs the sample cost matrix provided in the assignment. 
	matrix - Generates an n x n cost matrix with up to k values. 
	file - Runs a matrix defined in an external text file relative to assig.py. 
	quit - Ends the program.

Example Output - 
	The index in the array represents the cryptographer and the value represents the
	message they've been assigned to decrypt.

	Running exhaustive...
	---------------------------------
	[2, 1, 3, 4] 
	Exhaustive total cost: 13 

	Running greedy...
	---------------------------------
	[2, 3, 1, 4]
	Greedy total cost is: 14

Running a Custom Matrix - 
	Add a text file to the project directory separating each value with a space.
	Required format as follows:
				1 5 3 5
				2 3 2 5
				2 1 2 4
