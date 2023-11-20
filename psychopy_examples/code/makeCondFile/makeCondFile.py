import csv
import itertools

# make a conditions file that contains x columns with all permutations of list

#a list of possible conditions
myList=['LR20', 'LR80', 'UD20', 'UD80']

#get all permutations (of length 4)
allPerms = itertools.permutations(myList)

# Create a list of dictionaries to turn into a conditions file
toCSV=[]
for thisPerm in allPerms:
    toCSV.append({'Cond1':thisPerm[0], 'Cond2':thisPerm[1], 'Cond3':thisPerm[2], 'Cond4':thisPerm[3]})

#make a conditions file with keys as headers and values as rows
keys = toCSV[0].keys()
with open('conditions.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)