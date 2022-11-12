import csv

with open("students.csv","rt") as csv_file:

    dict={}

    reader = csv.reader(csv_file)
    
    next(reader)

    for row_list in reader:

        key = row_list[0]
          
        dict[key]=row_list
    
    print(dict)

    
   









