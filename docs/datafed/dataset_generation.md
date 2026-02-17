# Dataset Generation

Sometimes it is useful to have a large dummy dataset for testing and
benchmarking data transfer technologies. To get realistic results,
datasets filled with uncompressible random data are preferable to those
filled with zeros, as these may be automatically compressed by
filesystems or network infrastructure.

The Python script below automates the process of generating a number of
files with random contents. It requires Python 3.9 or higher. The first
argument is the dataset name. There are 4 preset datasets included,
which match the ones used so far for our Globus transfer tests.
Additional datasets can easily be added by appending them to the
`datasets` dictionary at the top of the script.

If a second argument is given, this will be the directory name in which
to generate the files. If it is not given, the dataset name will be used
for this.

Example usage:

```bash
python createdataset.py 50x100G my_dir
```

To use, copy the code below into a Python file:

```python
#!/usr/bin/env python
#
# Script to generate a set of files filled with pseudorandom numbers.
# Requires Python 3.9 or newer.
#
# Usage: createdataset.py <dataset name> [<directory>]
#
# The available datasets are given in the dictionary at the top of the script.
#

import os
import random
import sys

datasets = {
    "50x100G": {
        "numFiles": 50,
        "fileSize": "100G",
        "prefix": "test",
        "seed": 0
    },
    "500x10G": {
        "numFiles": 500,
        "fileSize": "10G",
        "prefix": "test",
        "seed": 0
    },
    "1000x1G": {
        "numFiles": 1000,
        "fileSize": "1G",
        "prefix": "test",
        "seed": 0
    },
    "50x10G": {
        "numFiles": 50,
        "fileSize": "10G",
        "prefix": "test",
        "seed": 0
    }
}

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
dataset_name = sys.argv[1] if len(sys.argv) >= 2 else None
if dataset_name is None or dataset_name not in datasets or len(sys.argv) > 3:
    print("Usage: createdataset.py <dataset name> [<directory>]")
    print("  Available datasets: " + ", ".join(datasets.keys()))
    sys.exit(1)

# look up dataset parameters
dataset = datasets[dataset_name]
directory = dataset_name if len(sys.argv) < 3 else sys.argv[2]
num_files = dataset["numFiles"]
file_size = parse_file_size(dataset["fileSize"])
prefix = dataset["prefix"]
seed = dataset["seed"]

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

Note that generating test data this way is significantly slower than
simply copying data out of `/dev/urandom` using a simple Bash command,
probably because Python is an interpreted language and its random
number generation may not be optimised for this use case. If speed of
generation is more important than reproducibility, this script may not
be the best solution.
