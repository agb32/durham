# The COSMA Museum

## A History of COSMA

COSMA is a high performance computing facility based at Durham University, dedicated towards 
particle physics, astronomy and cosmology research. It forms part of the UK's DiRAC facility.

The first version of the system, COSMA-1  was formally opened on 31st July 2001. Since then 
COSMA has gone through seven major hardware generations, with each one scaling up compute power, 
memory and storage to keep pace with the growing demands of cosmological simulation:

- **COSMA-1** (2001) - 64 SunBlade1000 nodes, 114 GFLOPS
- **COSMA-2** (2004) - 258 SunFire210 nodes, 516 GFLOPS
- **COSMA-3** (2006) - 258 SunFire2100 and 64 SunFire4100 nodes, 4 TFLOPS
- **COSMA-4** (2010) - 248 Intel Westmere nodes, 31 TFLOPS
- **COSMA-5** (2012) - 420 Sandy Bridge nodes, 140 TFLOPS
- **COSMA-6** (2016) - 528 Sandy Bridge nodes, 175 TFLOPS
- **COSMA-7** (2018) - 452 Skylake nodes, 445 TFLOPS
- **COSMA-8** - the current generation

### Brief history of COSMA 1-8

COSMA 1 was created in 2001, with 2TB of storage and 64 nodes of 2GB of RAM, alongside 128 cores.

COSMA 1 was then replaced by COSMA 2 in 2004, with 20TB of storage alongside 258 nodes, resulting 
in 516 cores total, with 1GB of RAM.

In 2006, COSMA 3 began its life, with 130TB of storage and 258 nodes with 2GB RAM working alongside 
64 nodes with 4GB of RAM, with a total of 644 cores across all nodes.

By 2010, COSMA 4 replaced COSMA 3, with 1.1PB of storage alongside 248 nodes with 64GB of RAM, and 
3968 cores.

COSMA 5 was established in 2012 with 2.5PB of storage paired with 420 nodes of 128GB of RAM for 6720 
total cores. COSMA 5 was refurbished in 2025, and was funded by a carbon reduction fund, alongside 
DELL and AMD.

COSMA 6 was next, where it ran alongside COSMA 5 from 2017, also having 2.5PB of storage, and had 
carried 528 nodes each with 128GB of RAM, and 8448 cores, 108 more nodes and 1728 more cores than 
the original COSMA 5. It actually began life in 2012 at the Hartree Centre in Cheshire, based on 
COSMA 5 hardware. COSMA 6 was retired in the April of 2023.

COSMA 7 was installed 2 years later, debuting in 2018 with 3.1PB of storage and 452 nodes each with 
512 GB of RAM per node and 28 cores(that's 12,656 cores!). At most a job can only use half of COSMA 7, 
as whilst one half of COSMA 7 uses infiniband fabric, the other half uses an advanced ethernet fabric.

COSMA 8's prototype began use in 2020 and entered service under a phase 2 extension in 2023, with 20PB 
of storage and 528 computer nodes each with 1TB RAM and 128 cores, meaning it has 528 TB of RAM with 
67,584 cores! COSMA 8 runs in excess of 200GB/second, more than 2,000 times that of a home network.

## The Museum

The COSMA museum is a display of a small physical collection of retired hardware which was used
in several generations of the machine. It is a cabinet of things which shows how much HPC hardware 
has changed over the past 26 years of COSMA.

### The 250GB disk
```{figure} ../images/museum_images/IMG_5057.jpeg
:width: 400px

The 250GB disks are smaller and were used for COSMA 5 in 2012. These are mostly used to store
metadata, rather than the contents of a file, as they are faster than disks with smaller capacity.
```

### Tape Storage
```{figure} ../images/museum_images/IMG_5058.jpeg
:width: 400px

The tapes are used to back up data and to archive data that is not required. They can be restored 
to disks if the data is needed again. The use of tapes for archiving data began in 2015, and today, 
there is 26 PB of tape storage.
```

### CX55A Adapter
```{figure} ../images/museum_images/IMG_5062.jpeg
:width: 400px

This VPI(Virtual Protocol Interconnector) adapter supports both EDR Infiniband as well as 100GbE Ethernet, 
and was used for COSMA 6. 
```

### Sunfire v210
```{figure} ../images/museum_images/IMG_5081.jpeg
:width: 400px

The Sunfire v210 was a server manufactured by Sun microsystems, announced in November 2005 and used 
in COSMA 3 (2006-2010). It takes up 1 rack unit and uses two 1.34 GHz UltraSPARC IIIi processors.
```

### More on disks
```{figure} ../images/museum_images/IMG_5080.jpeg
:width: 400px

There are a variety of companies that COSMA gets its disks from. Shown here are 3 of them: DotHill, Sun, and IBM.
```

### Right Side PDU(Power Distribution Unit)
```{figure} ../images/museum_images/IMG_5071.jpeg
:width: 400px

This PDU was utilised in 2012 for COSMA 5, and mounts on the right side of cabinets to maximise space.
```

### System x iDataPlex dx360 M4
```{figure} ../images/museum_images/IMG_5066.jpeg
:width: 400px

Released in 2013 by IBM, these compute nodes were utilised in COSMA 5 (2012-2025). They lie two on a unit 
rack, one on top of the other.
```

### Single-Phase Socket
```{figure} ../images/museum_images/IMG_5088.jpeg
:width: 400px

A single-phase socket rated for 230V and used to provide power to the COSMA servers.
```

### HP Procurve Switch 2848
```{figure} ../images/museum_images/IMG_5087.jpeg
:width: 400px

Released in 2004, utilised in COSMA 2 (2004-2006)
```

### COSMA 8 compute nodes
```{figure} ../images/museum_images/IMG_5092.jpeg
:width: 400px

COSMA 8 is our current supercomputer, housed in the Lydia Heck data centre. It started running in 2010. 
COSMA 8 consists of 520 nodes, each with 128 cores and 1TB RAM.
```

### Sunfire X4140
```{figure} ../images/museum_images/IMG_5094.jpeg
:width: 400px

The Sunfire X4140 was released in 2008, and utilised with COSMA 4 (2010-2012). The X4140 allowed 8 DDR-2 
DIMM slots per socket, and was capable of up to 800MHZ of memory speeds.
```

### Qlogic SANbox 5800 fibre channel switch
```{figure} ../images/museum_images/IMG_5083.jpeg
:width: 400px

The SANbox 5800 was released in 2008 and utilised in COSMA 4 (2010-2012). Switches connect nodes, allowing 
files to be sent from node to node through high speed transmission cables. Modern cables used in COSMA 8 
have transmission speeds up to 200Gb per second.
```
