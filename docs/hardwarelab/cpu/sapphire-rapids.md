# Sapphire Rapids

## Node access

Our Sapphire Rapids are configured to hold Ponte Vecchio GPUs (PVCs). Therefore, they are accessible as part of our Intel GPU nodes.

- Node name: gi001
- Permissions: [Intel GPU group](../access.md)
- Access mode (Slurm group): direct login through ssh from login8.cosma.dur.ac.uk (*)

(*) The nodes are given out FCFS, i.e. please check prior to any benchmarking that nobody else is currently using the node.

## Specification

- CPU name:       Intel(R) Xeon(R) Platinum 8480+
- Sockets:                2
- Cores per socket:       56
- Threads per core:       2

## Environment

As this is an Intel node while Cosma's login nodes are AMD, we recommend to compile exclusively on the node:


       module load intel_comp
       module load compiler-rt tbb compiler mpi

The module oneAPI should work as well.

## Performance

To assess the node's performance, we recommend to run

     module load likwid
     likwid-bench

Type in -a or -h to see an overview of the available metrics. Stream Triad and peak are the ones we usually recommend to look at first.



