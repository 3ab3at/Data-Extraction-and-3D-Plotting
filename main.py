import subprocess
import sys,os
sys.path.append(os.path.realpath('..'))

# Run the first Python script
subprocess.run(['python3', 'scripts/extract.py'])

# Run the second Python script
subprocess.run(['python3', 'scripts/dup.py'])

# Run the third Python script
subprocess.run(['python3', 'scripts/merge.py'])

# Run the fourth Python script
subprocess.run(['python3', 'scripts/plot.py'])