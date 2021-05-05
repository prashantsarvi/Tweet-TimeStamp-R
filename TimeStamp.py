import csv

from pandas import DataFrame
from pymongo import MongoClient
import datetime
import pandas as pd
import json

myclient = MongoClient("mongodb+srv://TwitterDB:twitterextraction@twittercluster.udioj.mongodb.net/test")
tweeterDb = myclient["ProcessedDB"]
Collection = tweeterDb["ProcessedTweet"]
x = Collection.find()
count = 0
constant = 86500
multiplier = 0.23
timestampList = []
timestampList1 = []
for i in x:
    count += 1
    if 'created_at' in i:
        createdTag = i['created_at']
        tagList = createdTag.split()
        if 'Nov' in createdTag:
            month = 11
        if 'Dec' in createdTag:
            month = 12

        string = str(tagList[2]) + '-' + str(month) + '-' + str(tagList[5])
        date = datetime.datetime.strptime(string, "%d-%m-%Y")
        timeStampConstant = datetime.datetime.timestamp(date)
        timeStamp = timeStampConstant + (constant * multiplier)
        multiplier += 1
        timestampList.append(str(timeStamp).split())
        if count == 151:
            break

file = open('sample.csv', 'w+', newline='')
title = ['T']
with file:
    write = csv.writer(file)
    write.writerows(title)
    write.writerows(timestampList)
