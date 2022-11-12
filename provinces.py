
def main():

    text_list = read_list("provinces.txt")
    print(text_list)

    text_list.pop(0)
    text_list.pop()
    length = len(text_list)
    for i in range(length):
        if text_list[i] == "AB":
            text_list[i]="Alberta"

            
    print(text_list)
    times = text_list.count("Alberta")
    print(times)




def read_list(file):

    with open ("provinces.txt","rt") as text_file:

        text_list = []

        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)
    
        return text_list




if __name__ == "__main__":
    main()
