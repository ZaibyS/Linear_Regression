# Linear_Regression

The following program implments machine learning algorithm Linear regression using Batch Gradient descent method.

Source file: Linear_Regression.py
CSV file: Random.csv

The program runs on console
The format to run the program is: python Linear_Regression.py --data random.csv --learningRate 0.0001 --threshold 0.0001


Format of CSV file is as following:
X1,X2,.....Xn,Y
where
X1: first variable
X2: second variable
....
Y: Target Variable


Output of the program is a CSV file of the following format:
iteration_number,[weight0,weight1,weight2,...,weightN],sum_of_squared_errors


Note: Delete the output file before running the program again,
as it would append the data at the end of the file each time you run the code.
