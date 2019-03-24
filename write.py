import csv
import sys

csvData = sys.argv[1]


with open('DB.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(csvData.split())

csvFile.close()
