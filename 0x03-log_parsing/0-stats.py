#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

# Initialize a dictionary to store status code counts
status_code_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

# Initialize variables to track total size and line count
total_size = 0
line_counter = 0

try:
    # Iterate through each line in stdin
    for line in sys.stdin:
        line_parts = line.split(" ")

        # Check if the line has enough parts
        if len(line_parts) > 4:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])

            # Increment the status code count if it's in the dictionary
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1

            # Update the total file size and line counter
            total_size += file_size
            line_counter += 1

        # Print metrics every 10 lines
        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_size))
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print('Interrupted by user')

finally:
    # Print final metrics before exiting
    print('File size: {}'.format(total_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print('{}: {}'.format(code, count))
