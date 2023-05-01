import re
import sys,os
sys.path.append(os.path.realpath('..'))

# Defining the enery reference for easier changing among different files
E_ref = 50.95273764

# Open input and output files
with open('input_file.txt', 'r') as infile, open('data/DMF_extracted.txt', 'w') as outfile1, open('scripts/radius_post_extraction.txt', 'w') as outfile2, open('data/angle_extracted.txt', 'w') as outfile3:
    # Loop through each line in the input file
    for line in infile:
        # Use regular expression to match lines starting with "!Density functional" and capture the number after the spaces
        match1 = re.match(r'^\s*!Density functional\s+([\d\.\-]+)', line)
        if match1:
            # Write the captured radius to the output file
            outfile1.write(str(abs(abs(float(match1.group(1))) - E_ref)) + '\n')
        match2 = re.match(r'^\s*DO\s+R\s+=\s+(.+)', line)
        if match2:
            # Write the captured angle to the output file
            outfile2.write(match2.group(1) + '\n')
        match3 = re.match(r'^\s*DO\s+PHI\s+=\s+(.+)', line)
        if match3:
            # Write the captured number to the output file
            outfile3.write(match3.group(1) + '\n')
