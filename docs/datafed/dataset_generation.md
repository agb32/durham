# Dataset Generation

Sometimes it is useful to have a large dummy dataset for testing and
benchmarking data transfer technologies. To get realistic results,
datasets filled with uncompressible random data are preferable to those
filled with zeros, as these may be automatically compressed by
filesystems or network infrastructure.

The Python script below automates the process of generating a number of
files with random contents. It requires Python 3.9 or higher. The first
argument is the dataset name. There are a number of preset datasets included,
which match the ones used so far for our Globus transfer tests.
Additional datasets can easily be added by appending them to the
`datasets` dictionary at the top of the script.

If a second argument is given, this will be the directory name in which
to generate the files. If it is not given, the dataset name will be used
for this.  See --help for additional options.

Example usage:

```bash
python datagenerator.py 50x100G my_dir
```

The code is available at [https://gitlab.cosma.dur.ac.uk/cosma/datagenerator](https://gitlab.cosma.dur.ac.uk/cosma/datagenerator)


Note that generating test data this way is significantly slower than
simply copying data out of `/dev/urandom` using a simple Bash command,
probably because Python is an interpreted language and its random
number generation may not be optimised for this use case. If speed of
generation is more important than reproducibility, this script may not
be the best solution.
