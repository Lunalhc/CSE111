import csv


def main():

    I_number= input("Enter the I-number:")
    I_number = I_number.replace(" ","")

    read_dict("students.csv")

    list = read_dict("students.csv")

    if I_number in list:

        name = list[I_number] 

        print(name)

    else:
        print("no such students")tr




def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    with open(filename,"rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        students_dict={}

        for rows in reader:
            
            key = rows[0]
            value = rows[1]

            students_dict[key] = value
    
    return students_dict
            
if __name__ =="__main__":

    main()






