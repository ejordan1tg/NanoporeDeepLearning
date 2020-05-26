import pandas as pd
import pyabf
import csv
from keras_preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

# DO NOT EDIT
# THIS IS A TEMPLATE FOR FINDING EVENTS OF A SPECIFIC LENGTH
def dataPoints(abfFile ,sheet, newCSVname, statsFile):
    abf = pyabf.ABF(abfFile)
    eventLengths = []
    eventLengths1 = []
    with open(newCSVname, mode='w') as csvNew:
        writer = csv.writer(csvNew, delimiter=',')
        frame = pd.read_excel(sheet)
        start = frame['Event Start'].dropna()
        end = frame['Event end'].dropna()
        for n in range(len(start)):
            eventStats = []
            eventStart = int(start[n]/.05)
            eventEnd = int(end[n]/.05)
            lengthEvent = eventEnd-eventStart
            counter = 0
            if((lengthEvent > 0) and (lengthEvent <= 2000)):
                # print(start[n], end[n])
                for n in range(eventStart, eventEnd):
                        X = abf.sweepX[n]
                        Y = abf.sweepY[n]
                        eventStats.append(Y)
                        counter += 1
                for n in range(len(eventStats), 2000):
                        eventStats.append(0)
                        counter += 1
            writer.writerow(eventStats)
            eventLengths.append(counter)
        print(eventLengths)
        csvNew.close()
    file = open(statsFile, 'a')
    file.write('\n')
    file.write("Event count for " + newCSVname)
    file.write('\n')
    for i in range (0, len(eventLengths)-1):
        if(eventLengths[i] != 0):
                eventLengths1.append(eventLengths[i])
    print(eventLengths1)
    file.write(str(len(eventLengths1)))


# # THIS IS A TEMPLATE FOR FINDING EVENTS OF ALL SIZES
# def dataPoints(abfFile ,sheet, newCSVname, statsFile):
#     abf = pyabf.ABF(abfFile)
#     eventLengths = []
#     with open(newCSVname, mode='w') as csvNew:
#         writer = csv.writer(csvNew, delimiter=',')
#         frame = pd.read_excel(sheet)
#         start = frame['Event Start'].dropna()
#         end = frame['Event end'].dropna()
#         for n in range(len(start)):
#             eventStats = []
#             eventStart = int(start[n]/.05)
#             eventEnd = int(end[n]/.05)
#             lengthEvent = eventEnd-eventStart
#             pointCounter = 0
#             for n in range(eventStart, eventEnd):
#                     X = abf.sweepX[n]
#                     Y = abf.sweepY[n]
#                     eventStats.append(Y)
#                     pointCounter += 1
#             writer.writerow(eventStats)
#             eventLengths.append(pointCounter)
#         print(eventLengths)
#         csvNew.close()
#     file = open(statsFile, 'a')
#     file.write('\n')
#     file.write("Event count for " + newCSVname)
#     file.write('\n')
#     file.write(str(len(eventLengths)))




