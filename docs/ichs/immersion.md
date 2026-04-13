# Immersion tank system

Immersion cooling of HPC equipment offers a low carbon, energy efficient route for data centre operation.

![The immersion tank](../images/immersiontank.jpg)
![Servers in the immersion tank](../images/immersionservers.jpg)

## Details

### Tank

A 50U MIDAS immersion tank with forced convection was selected.  Vespertec were the integrator.  This is to be housed within the existing data centre, with installation in May 2025.

### Servers

The immersion tank will initially contain 6 servers:

 - 5x nodes each with dual AMD Bergamo processors and 1.5TB RAM (256 cores per node)
   - 100G InfiniBand connectivity to an existing network fabric
 - 1x node with dual Intel Sapphire Rapids processors and a NVIDIA H100 GPU

Additional kit will be hosted within the tank in due course.

### COSMA5 replacement

The COSMA5 HPC system was installed in Durham in 2012, and was registered on the TOP500 list of fastest supercomputers at 134th position.  

With 16 cores and 128GB RAM per node, and around 320 nodes, this system was initially part of the DiRAC national HPC service, before being converted to a Durham-only system in 2018.

In 2024, as a result of a Durham University carbon fund and a contribution from Dell and AMD, 48 nodes were replaced with three new nodes with an equivalent core count and RAM footprint.  This formed the basis of a new COSMA5 system.

The 5 nodes hosted within the immersion tank then allowed for the complete replacement of COSMA5.  The new COSMA5 system will therefore include:

- 8x nodes each with dual Bergamo processors, 256 cores and 1.5TB RAM per node
- A total of 2048 cores and 12TB RAM
- 8kW power peak (typical 4kW)

This replaces the older system which had
- 420x nodes each with dual Intel Sandybridge processors, 16 cores and 128GB RAM per node
- A total of 6720 cores and 52TB RAM
- 140kW power

Although the new COSMA5 system has fewer than one third of the cores, the overall performance is within a factor of two due to faster cores and AVX512 registers.  It is significantly more power efficient, an improvement of nearly 20x.

The immersion tank system therefore allows COSMA5 to continue operation into the 2030s.
