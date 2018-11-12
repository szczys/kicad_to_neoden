from __future__ import print_function

#Translator for converting KiCAD .pos files to .csv files for a NEODEN pick and place machine
#Paste relevant rows of the .pos files below and chance the trailing_letter
#to be "T" for top or "B" for bottom

import fileinput
import os

def transrotate(value):
	if value <= 180:
		return int(value)
	else:
		value -= 180
		return int(0-(180-value))

def process_pos_lines(pos_lists):
        output_string = "Designator,Footprint,Mid X,Mid Y,Layer,Rotation,Comment\n"
        output_string += ",,,,,,\n"
        for line in pos_lists:
                if line[0][0] == '#':
                        continue
                outline = line[0] + "," + line[1] + ","
                outline += line[3].split('.')[0] + "." + line[3].split('.')[1][:2] + "mm,"
                outline += line[4].split('.')[0] + "." + line[4].split('.')[1][:2] + "mm,"
                if line[-1] == "top":
                        outline += "T,"
                else:
                        outline += "B,"
                outline += str(transrotate(float(line[5]))) + "," + line[2]
                output_string += outline + '\n'
        return output_string

def main():
        #Turn input .pos file into a list of lists
        pos_lines = list()
        for line in fileinput.input():
                pos_lines.append(line.strip('\n').split())

        cur_dir = os.getcwd()
        filename = fileinput.filename()
        if filename[-4:] != ".pos":
                print("WARNING: Input file doesn't have expected '.pos' extension")
        print("Parsing " + filename)

        neoden_format = process_pos_lines(pos_lines)
        #Strip trailing newline character
        if neoden_format[-2:] == '\n':
                neoden_format = neoden_format[:-2]

        print("Writing CSV file")
        output_file = os.path.splitext(os.path.join(cur_dir,filename))[0]+"_neoden.csv"

        with open(output_file, 'w') as ofile:
                ofile.write(neoden_format)
        print("Successfully wrote:",output_file)

if __name__ == '__main__':
        main()
