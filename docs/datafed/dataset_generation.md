# Dataset Generation

Sometimes it is useful to have a large dummy dataset for testing and benchmarking data transfer technologies. To get realistic results, datasets filled with uncompressible random data are preferable to those filled with zeros, as these may be automatically compressed by filesystems or network infrastructure.

The Python script below automates the process of generating a number of files with random contents. It requires Python 3.9 or higher. The random seed can be specified, allowing the datasets to be reproduced if required. The script takes the following arguments. The first three are required and the final two are optional:

- The directory in which to generate the files. This will be created if it does not already exist.
- The number of files to generate.
- The size of each file. This may be given in bytes, or a 'K', 'M' or 'G' suffix may be used to denote kilobytes, megabytes or gigabytes.
- The filename prefix to use. Defaults to 'test'.
- The random seed to use. Defaults to 0.

Example usage:

```bash
python createdataset.py dataset1 100 10G myfile 42
```

To use, copy the code below into a Python file:

```python
#!/usr/bin/env python
#
# Script to generate a set of files filled with pseudorandom numbers.
# Requires Python 3.9 or newer.
#
# Usage: createdataset.py <directory> <number of files> <size of one file> \
#            [<filename prefix> <random seed>]
#
# directory is the name of the directory in which to create the files.
# file size may be given in bytes or with a K, M, or G suffix for kilobytes,
#   megabytes or gigabytes.
# filename prefix is the stem used for each filename. A numeric suffix will be
#   appended for each file. This is optional and the default is 'test'.
# random seed is the seed for the random number generator, to allow reproducibility.
#   This is optional and the default is zero.
#

import os
import random
import sys

# how many bytes to write to the file at once
MAX_BLOCK_SIZE = 1000000

# Parses a string containing a file size. Deals with the optional K, M or G suffix
# and returns the size as an integer
def parse_file_size(szstr):
    multiplier = 1
    szstr = szstr.upper()
    if szstr[-1] == 'K': multiplier = 1000
    elif szstr[-1] == 'M': multiplier = 1000000
    elif szstr[-1] == 'G': multiplier = 1000000000
    if multiplier != 1: szstr = szstr[:-1]
    return int(szstr) * multiplier


# process arguments
if len(sys.argv) < 4 or len(sys.argv) > 6:
    print("Usage: createdataset.py <directory> <number of files> <size of one file> [<filename prefix> <random seed>]")
    sys.exit(1)

try:
    directory = sys.argv[1]
    num_files = int(sys.argv[2])
    file_size = parse_file_size(sys.argv[3])
    prefix = "test"
    seed = 0

    if len(sys.argv) > 4: prefix = sys.argv[4]
    if len(sys.argv) > 5: seed = int(sys.argv[5])
except ValueError:
    print("Error: file count, file size and random seed must be integer values")
    sys.exit(1)

# seed the random number generator
random.seed(seed)

# create output directory if it doesn't exist
if os.path.exists(directory):
    if not os.path.isdir(directory):
        print(f"Error: {directory} already exists but is not a directory")
        sys.exit(1)
else:
    os.mkdir(directory)

print(f"Generating {num_files} files of size {file_size} in directory {directory}")

# loop over files to generate
for i in range(num_files):
    filename = f"{directory}{os.path.sep}{prefix}{i:06}"
    print(f"Generating file {filename}")
    bytecount = 0
    f = open(filename, "wb")
    while bytecount < file_size:
        block_size = file_size - bytecount
        if block_size > MAX_BLOCK_SIZE: block_size = MAX_BLOCK_SIZE
        data = random.randbytes(block_size)
        f.write(data)
        bytecount += block_size
    f.close()
```

Note that generating test data this way is significantly slower than simply copying data out of `/dev/urandom` using a simple Bash command, probably because Python is an interpreted language and its random number generation may not be optimised for this use case. If speed of generation is more important than reproducibility, this script may not be the best solution.
