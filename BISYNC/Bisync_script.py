from pathlib import Path
import sys

def bisync_hex(hex : str) -> str:
    # STX + hex with replacing any 03 with DLE's + ETX
    return "02" + hex.replace("03", "1003").strip() + "03\n"

input_hex = []

# Find where this file is in your current directory and use the .parent
current_dir = Path(__file__).parent

# Input file handling
filepath = r"{}/input.hex".format(current_dir)
try:
    with open(filepath, 'r') as input_file:
        # read the file into a list
        input_hex = input_file.readlines()

except FileNotFoundError: # See if the file is not found here
    print(f"File is not in the path {filepath}")
    
    # don't run any more code, exit the python file from executing
    sys.exit()

# blocks are for handling each hex and putting sentinals in it and appending it to a list

print(f"The input data is {input_hex}")
res = []
for hex in input_hex:
    tmp = bisync_hex(hex)
    res.append(tmp)

print(f"The output data is {res}")


outputFile_Path = r"{}/output.bisync".format(current_dir)
try:
    # This overwrites existend data, if we don't wanna do that, put it in append mode
    with open(outputFile_Path, 'w') as outputFile:
        # The file won't be able to make write a list to a file, so convert to a string
        output_bisyn = "".join(res)

        # write to the file
        outputFile.write(output_bisyn)

except IOError: # Detect if for some reason this file can't write an output file
    print(f"Can't write to file {outputFile_Path}")