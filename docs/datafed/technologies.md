# Data transfer technologies

We are investigating a number of data transfer technologies, with significant emphasis on the user perspective and ease of use.  We will capture information about where these can be used, what performance is likely to be achieved, and how they should be used to speed up data transfer

These include:

- [Rsync](rsync.md)
- [Rclone](rclone.md)
- [Globus](globus.md)
- [RUCIO](rucio.md)

We will also investigate other technologies such as:

- [Pelican](https://pelicanplatform.org/)
- [EU datahub](https://datahub.egi.eu/)
- [OneData](https://github.com/onedata)
- [EU Open Science Cloud](https://research-and-innovation.ec.europa.eu/strategy/strategy-research-and-innovation/our-digital-future/open-science/european-open-science-cloud-eosc_en)
- [EUDat](https://eudat.eu/)


With these, we will provide some input into the UK DRI federation landscape survey, but not seek to implement or test.

There are also various technical tools and settings that can help improve performance.  For example:

- [Setting the MTU size](mtu.md)



# Use cases

## VIRGO

## SKA UKSRC

## UKAEA

## LSST / Vera C. Rubin Telescope

# Other use cases

## CryoEM

CryoEM datasets are increasing in size significantly, and so makes a useful case to study.

## National X-ray CT

The [National Xray CT](NXCT.ac.uk) Phase 2 EPSRC grant has
just been awarded; and part of future work in the next five years is
large data transfer between sites including Diamond Light Source -
Manchester, UCL, Warwick and Southampton - so Globus is a strong
possible choice.


## The EU Open Science Cloud

## Tessera

The [Tessera](https://github.com/ucam-eo/tessera) project requires a large data volume, based at Cambridge.

# Tips

Some simple tips and tricks to aid data transfer

## Small files

Improved performance can often be achieved by tarring many small files into a larger one before transfer.

## Source and destination file systems

Selecting the correct file system at either end can help with transfer speed - slow file systems may not be able to keep up with the network transfer.

