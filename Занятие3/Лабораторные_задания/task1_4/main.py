INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            for upper_line in map(str.upper, input_file):
                output_file.write(upper_line)

#with open(INPUT_FILE,"r") as ifile, open(OUTPUT_FILE,'w') as ofile:
    #ofile.write(ifile.read().upper())
#with open('input.txt') as f:
    #with open('output.txt', "w") as fi:
        #for x in f:
            #fi.write(x.upper())

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
