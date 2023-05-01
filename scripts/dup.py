import sys,os
sys.path.append(os.path.realpath('..'))
# Open input and output files
with open('scripts/radius_post_extraction.txt', 'r') as infile, open('data/radius_extracted.txt', 'w') as outfile:
    # Loop through each line in the input file
    for line in infile:
        # Write the original line to the output file
        outfile.write(line)
        
        # Write 5 additional copies of the line to the output file
        for i in range(6):
            outfile.write(line)