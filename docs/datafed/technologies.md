# Data transfer technologies

We are investigating a number of data transfer technologies, with significant emphasis on the user perspective and ease of use.  We will capture information about where these can be used, what performance is likely to be achieved, and how they should be used to speed up data transfer.  

These include:

- [Rsync](rsync.md)
- [Rclone](rclone.md)
- [Globus](globus.md)
- [RUCIO](rucio.md)

## rsync

rsync is a simple tool for transferring directory structures and files between two end points.

## rclone

rclone is a commonly used tool in cloud-land, used to transfer files to and between object stores.

## Globus

Globus is a data transfer management tool which is used to orchestrate data movement between remote sites.

## RUCIO

RUCIO is a policy-driven data management tool which is used to orchestrate data movement between remote sites.

## Dataset generation

We will perform data transfer tests using known, repeatable datasets.  To this end, we provide a [dataset generator](dataset_generator.md) which can be used to  generate the datasets used on any platform such that repeatable tests can be performed.

## Collaborative documentation

This documentation is collaborative: if you have measurements or information which can be added, please do so.

## Other data transfer technologies

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

This project is producing a 1PB AI model from the 200PB Sentinal 1 and 2 data.  The data processing is open source.  Chunks of satellite data are downloaded and modelled to a 10x10m square, covering the whole planet, delivering 1PB of inference data.

This project is currently the largest user of the DAWN AI system, and can saturate the University of Cambridge external network link.

The raw data is hosted on Azure, and a [custom Python script](https://github.com/ucam-eo/tessera/blob/alpha_version_1.0/tessera_preprocessing/s1_s2_downloader.sh)  is used for downloading the data to the Cambridge CSD3 system, based on urllib3 and the Python requests library.

# Tips

Some simple tips and tricks to aid data transfer

## Small files

Improved performance can often be achieved by tarring many small files into a larger one before transfer.

## Source and destination file systems

Selecting the correct file system at either end can help with transfer speed - slow file systems may not be able to keep up with the network transfer.

