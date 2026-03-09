# RUCIO

RUCIO is a data transfer platform developed for CERN, and becoming more widely used.  It has a powerful policy engine which is used to determine when transfers take place.

## RUCIO server

A RUCIO server is running at EPCC.

## RUCIO end points

We have end points at:
 - RAL
 - COSMA HPC
 - COSMA StorJ cloud

## RUCIO Python client

To install the RUCIO Python client, the following rpm packages are needed:
 - cmake doxygen glib2-devel libattr-devel openldap-devel zlib-devel srm-ifce-devel dcap-devel globus-gass-copy-devel davix-devel xrootd-client-devel libssh2-devel gtest-devel gfal2-plugin-dcap python3-gfal2 python3-gfal2-util

A Python client is then installed in a Python virtual environment using `pip install rucio-clients`.

Testing can be done using `rucio --account $USER --auth-host ukdac.rucio.lsst.ac.uk:data  -S oidc -v whoami`
and
`rucio -v upload --rse DATAFED-S3-DURHAM --scope user.$USER file.txt`
