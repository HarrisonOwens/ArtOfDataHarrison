import csv
import random

"""
1. Avg speed of all digimon
2. Function to count number of digimon with a specific attribute
3. Function finding team of digimon above certain atk power and below certain memory level
3. Describe process of working on these questions and hwo you worked with
"""

def avg_speed():
    with open("datasets/digimon.csv") as f:
        data = csv.DictReader(f)
        total_speed = 0
        count = 0
        f.seek(1)
        for row in data:
            speed = int(row["Spd"])
            count += 1
            total_speed += speed
        return total_speed / count

def attribute_count(column, attribute):
    with open("datasets/digimon.csv") as f:
        data = csv.DictReader(f)
        counter = {}
        f.seek(1)
        for row in data:
            if row[column] in counter.keys():
                counter[row[column]] += 1
            else:
                counter[row[column]] = 0
        keys_lower = []
        for i in counter.keys():
            keys_lower.append(i.lower())
        if attribute.lower() in keys_lower:
            return(counter[attribute])
        else:
            return("Use a valid attribute")

def teamMaker(memory_max, atk_min, spread):
    with open("datasets/digimon.csv") as f:
        data = csv.DictReader(f)


print(attribute_count("Type", "Vaccine"))
