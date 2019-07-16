import sys 
import csv
import string

def ReadAndOrganize():
	
	global targetValue
	global rows
	global cols
	global weights
	global hypothesisAnswer
	global xValues
	global gradients
		
	xValues = []
	targetValue = []
	rows = 0
	cols = 0
	weights = []
	gradients = []
	hypothesisAnswer = []
	i = 0
	currentLine = []
	

	for line in inputFile:
		currentLine.insert(i,line.split(","))
		i = i+1
	
	
	#currentLine now has x0,x1,x2...,y
	#float(currentLine[0][1] is one value from table
	#len(currentLine) means all the rows
	#len(currentLine[0]) means all the columns
	rows = len(currentLine)
	cols = len(currentLine[0])
	
	
	#initialization of xVlues rows
	xValues = [0] * rows
	for x in range(rows):
			#y values entry
		targetValue.insert(x,currentLine[x][cols-1])
			#xVlaues columns declaration
		xValues[x] = [0] * (cols-1)
			#xValues Entries
		for y in range(cols-1):
			xValues[x][y] = currentLine[x][y]
			
	weights = [0] * cols
	gradients = [0] * cols
	hypothesisAnswer = [0] * rows
		
	
def CalculateHypothesisAnswer():
	for x in range(rows):
		hypothesisAnswer[x] = 0
		for y in range(cols):
			if (y == 0):
				hypothesisAnswer[x] = float(hypothesisAnswer[x]) + (float(weights[y]) * float(1))
			else:
				hypothesisAnswer[x] = float(hypothesisAnswer[x]) + (float(weights[y]) * float(xValues[x][y-1]))


def SumOfSquaredErrors():
	sumOfSquaredErrors = 0
	for x in range(rows):
		sumOfSquaredErrors = sumOfSquaredErrors + ((float(hypothesisAnswer[x]) - float(targetValue[x])) * (float(hypothesisAnswer[x]) - float(targetValue[x]))) 
	
	return sumOfSquaredErrors

	
	
def CalculateGradient():
	for x in range(cols):
		gradients[x] = 0
		for y in range (rows):
			if (x == 0):
				gradients[x] += 1 *  (float(targetValue[y]) - float(hypothesisAnswer[y]))
			else:
				gradients[x] += float(xValues[y][x-1]) * (float(targetValue[y]) - float(hypothesisAnswer[y]))
	
def UpdateWeights():
	for x in range(cols):
		weights[x] = float(weights[x]) + (float(learningRate) * float(gradients[x]))
	

	
def Main(location, lR, thresh):
	global inputFile
	global learningRate
	global threshhold
	
	sumOfPreviousErrors = thresh + 1
	sumOfSqErrors = 0
	inputFile = open(location)
	learningRate = lR
	threshhold = thresh
	i = 0
	ReadAndOrganize()
	
	while (((float(sumOfPreviousErrors) - float(sumOfSqErrors)) > float(threshhold)) or i < 2):
		CalculateHypothesisAnswer()
		sumOfPreviousErrors = sumOfSqErrors
		sumOfSqErrors = SumOfSquaredErrors()
		i = i+1
		CalculateGradient()
		UpdateWeights()
		row = [i,weights,sumOfSqErrors]
		with open('output.csv', 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)
	csvFile.close()
	
if __name__ == "__main__":	
	Main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))