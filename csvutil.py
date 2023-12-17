# Utilities for dealing with csv files
import csv

# This will read in a file consisting of single word headers and 
# columns of floating point numbers

def readfloatfile(filename):
# Read the data in the csv file
	with open(filename,'r') as file:
		reader = csv.reader(file,delimiter=',')
		data = {}
		header = next(reader)
		ncol = len(header)
		nrow = 0
		for name in header:
			data[name]=[]
		for row in reader:
			for i, value in enumerate(row):
				data[header[i]].append(float(value))
			nrow += 1
		return header,data
		
