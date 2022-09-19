#!/usr/bin/env python
import argparse
import sys


def parse_args():
    parser=argparse.ArgumentParser(description="a script to do stuff")
    parser.add_argument("filename")
    args=parser.parse_args()
    return args

def convertToARFF(filename):
    print("Coverting ", filename, "to ARFF")


    minAttribute = 0
    maxAttribute = 41269

    #open a file for writing
    output = open("korsarak.arff", "wb")

    #write the header.
    output.write(b"@relation kosarak\n") #@relation Line


    for i in range(0,maxAttribute+1): #@attribute Lines
        s = f"@attribute a{i} " + "{0,1}\n"
        s = s.encode('ascii')
        output.write(s)

    output.write(b"@data\n") # @data line

    #reread our input file.
    dataPath = filename
    dataFile = open(dataPath, 'r')

    #for each line in our input file, write a line to our output
    # that is like {someNumber 1, someOtherNumber 1, anotherNumber 1}\n
    currentIndex = 0
    while True:
        line = dataFile.readline()
        if not line:
            output.close()
            break
        itemsInLine = line.split()
        intList = []
        for item in itemsInLine:
            intList.append(int(item) - 1)
        intList = [*set(intList)]
        intList.sort()
        stringToWrite = "{"
        for item in intList:
            stringToWrite = stringToWrite + f"{item} 1,"
        stringToWrite = stringToWrite.rstrip(stringToWrite[-1])
        stringToWrite = stringToWrite + "}\n"
        stringToWrite = stringToWrite.encode('ascii')
        output.write(stringToWrite)


def main():
    inputs=parse_args()
    convertToARFF(inputs.filename)


if __name__ == '__main__':
    main()

#%%
