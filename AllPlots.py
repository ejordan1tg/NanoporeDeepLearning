import pandas as pd
import pyabf
import csv
import matplotlib.pyplot as plt
import pyabf
from Plot2 import PLOT

def allPlots(abfFile ,sheet,name):
    frame = pd.read_excel(sheet)
    start = frame['Event Start'].dropna()
    end = frame['Event end'].dropna()
    for n in range(len(start)):
        eventStart = int(start[n]/.05)
        eventEnd = int(end[n]/.05)
        # PLOT(abfFile, eventStart, eventEnd)
        abf = pyabf.ABF(abfFile)
        xArray = []
        yArray = []
        for n in range(int(eventStart), int(eventEnd)):
            X = abf.sweepX[n]
            Y = abf.sweepY[n]
            # print("x:")
            # print(X)
            xArray.append(X)
            yArray.append(Y)
        plt.figure(figsize=(8, 5))
        plt.title("ABF File: " + abfFile + "\n" + "startTime: " + str(eventStart) + " endTime: " + str(eventEnd))
        plt.plot(xArray, yArray)
        resultsto = 'C:/Users/Elijah/Documents/NanoporeData/AllPlots/nome/'
        plt.savefig(resultsto + name + str(eventStart) + str(eventStart) + ".png")
        # plt.show()