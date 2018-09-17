import csv
import sys


def books1():
    fileName = sys.argv[1]
    allBookData = []
    with open('books.csv', newline='') as f:
        fileReader = csv.reader(f)
        print('test')
        for row in fileReader:
            #allBookData.append(parseBookData(row))
            print(row)
books1()
# def parseBookData(titleYearAuthor)
#    singleBookData = []
#    singleBookData = titleYearAuthor.split(",")
