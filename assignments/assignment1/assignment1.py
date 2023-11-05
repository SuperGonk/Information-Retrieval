import re
import pandas as pd
from collections import Counter


def taskA(data):

    #collect all rows with the given passage id.
    res = []
    count = 0
    for row in data["passageID"]:
        if row == 8004107:
            res.append(count)
        count += 1

    #Print wanted information.
    print("taskA:")
    for i in range(len(res)):
        current = data["passage"][res[i]]
        print("passage length: " + str(len(current.split())))
        print("character count: " + str(len(current)))
    print("\n")

def taskB(data):
    count = 0
    for row in data["queryID"]:
        if row == 494835:
            res = count
            break
        count += 1
    passage = data["passage"][count]
    passageID = data["passageID"][count]
    
    print("taskB:")
    print("passage: " + passage)
    print("passageID: " + str(passageID))


def taskC(data):
    counter = Counter(list(data["passageID"]))
    tupelList = []
    for item in counter.items():
        tupelList.append((item[0],item[1]))

    tupelList.sort(key=lambda a: a[1])
    maxTupel = tupelList[-1]


    counts = []
    count = 0
    for row in data["passageID"]:
        if row == tupelList[-1][0]:
            counts.append(count)
        count += 1
    
    print("taskC:")
    print("rowIDs of the passages: " + str(counts))
    querys = []
    for i in range(len(counts)):
        querys.append(data["queryID"][counts[i]])
    print("queryIDs of the passages: " + str(querys))
    

def main() -> None:
    FILEPATH = "msmarco-passagetest2019-top1000.tsv"
    passagetestCSV = pd.read_csv(FILEPATH, sep='\t', names = ["queryID", "passageID", "query", "passage"])
    collectionCSV = pd.read_csv(FILEPATH, sep='\t')

    #a solution
    taskA(passagetestCSV)
    # print(taskA(collectionCSV))

    #b solution
    taskB(passagetestCSV)
    # print(taskB(collectionCSV))

    #c solution 
    taskC(passagetestCSV)
    # taskC(collectionCSV)

main()