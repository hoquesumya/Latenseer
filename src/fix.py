import csv

# Define the input and output file paths
input_file = "/Users/sumyahoque/LatenSeer/src/rps10/s0.1/mix136/local_collect.csv"
output_file = "local_collect.csv"

# Open the input file in read mode and output file in write mode
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Replace all occurrences of ",MongoUpdate.," with ",MongoUpdate,"
        fixed_line = line.replace(",MongoUpdate.,", ",MongoUpdate,")
        outfile.write(fixed_line)

print("The file has been fixed and saved as", output_file)




