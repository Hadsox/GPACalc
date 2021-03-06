"""
GPACalc
Alex
3/5/2017

This module preforms all the calculations of the GPACalc program
functions in this module:
gpaCalc() -- calculates the gpa
totalGradePoint() -- sums the total grade points
totalCredits() -- sums the total credit hours
"""

# Global dictionary of the weight of the letter grades
grades = {'A': 4., 'a': 4., 'B': 3., 'b': 3., 'C': 2., 'c': 2., 'D': 1., 'd': 1., 'F': 0., 'f': 0.}


def gpaCalc(classes):
	"""
	Take in an array of classes, with the format of (# credit hours Grade) and returns the grade point average

	makes calls to the totalCredits() and totalGradePoint() to calculate the total number of credits and grade points

	:param classes: Array like
			a list of tuples with the format of (credit hours, letter grade)
	:return: gpa: float
			returns the gpa calculated
	"""
	total_grades = 0

	for i in classes:
		
		if i.split(' ')[-1] in grades:
			total_grades += int(i.split(' ')[0]) * grades[i.split(' ')[-1]]
		else:
			total_grades += (int(i.split(' ')[-1]))
	
	if total_grades == 0:
		return 0
	
	gpa = total_grades / totalCredits(classes)

	return gpa


def totalGradePoint(classes):
	"""
	Take in an array of classes, with the format of (# credit hours Grade) and counts the total number of grade points.

	:param classes: Array like
			a list of tuples with the format of (credit hours, letter grade)
	:return: totalgradepoints: int
			returns the sum of all the total grade points in the passed parameter.
	"""

	grade_sum = 0

	# summing the 24 index is the location of the letter grade, should look into a better way of doing this, in the event
	# formatting changes

	for i in classes:
		
		if i.split(' ')[-1] in grades:
			grade_sum += grades[i.split(' ')[-1]]
		else:
			grade_sum += int(i.split(' ')[-1])

	return grade_sum


def totalCredits(classes):
	"""
	Take in an array of classes, with the format of (# credit hours Grade) and counts the total number of credit hrs.

	:param classes: Array like
			a list of tuples with the format of (credit hours, letter grade)
	:return: totalcredits: int
			returns the sum of all the total credit hours in the passed parameter.
	"""

	total = 0

	# summing the 0 index of the tuple is equivalent to summing the integer credit hours
	for i in classes:
		total += int(i.split(' ')[0])

	return total

