import csv

with open("datasets/sentiment_data.csv", newline="", encoding="utf-8") as file:
    # reader = csv.reader(file, delimiter=" ", quotechar="|")
    reader = csv.reader(file, delimiter=",", quotechar="|")
    # reader = csv.DictReader(file)
    i=0
    for row in reader:
        print(row)
        i+=1
        if i > 200:
            break