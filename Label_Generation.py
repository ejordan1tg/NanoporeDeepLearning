import csv

def genLabels(nome, oneme):
    with open("Dataset_Labels.csv", mode= 'w') as labelCSV:
        writer = csv.writer(labelCSV, delimiter = ',')
        counter = 1
        for n in range(nome):
            writer.writerow(str(0))
            counter += 1
        for n in range(counter, oneme+1):
            writer.writerow(str(1))
    labelCSV.close()
