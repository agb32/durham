# NetworkPlus Federated Compute Services data federation project

## Overview

This project looks at large scale data movement between, into and out
of UKRI DRI sites, addressing a fundamental impediment in the form of
researcher-led, large-scale, distributed data management. Led by the
requirements of several high-priority science cases from fusion
energy, cosmology and survey astronomy, and engaging key players from
the UK DRI landscape, we will develop good practice and technology
demonstrators, to inform the UK federated-computing landscape as well
as to provide tangible guidance to researchers on how to take control
of their data requirements and exploit the potential offered by UK
investment in DRI.

Many of the most significant advances in computational science, in the
coming years, will rely on researchers being able to efficiently and
effectively control large amounts (Petabytes) of scientific data. New
machine-learning techniques are naturally data intensive and
international-scale scientific facilities such as laser facilities,
telescopes, and prototype fusion reactors all produce rich and complex
measurement and observational data.

It should be straightforward for a researcher to access and manipulate
datasets of this scale: UK Digital Research Infrastructure (DRI) is
linked by a state-of-the-art research network and key UK institutions
and facilities have cutting edge data-storage and data-analysis
services. However, the day-to-day reality for most researchers is much
less clear cut and there is a significant risk that UK-led,
world-class research will be stifled by an inability to access, move,
and manipulate scientific data with a low access barrier.

Researchers face bottlenecks and barriers in their attempts to
undertake data-intensive research. Issues related to the availability
and readiness of data-management technologies, concerns around data
security and access permissions, and the inability to orchestrate
distributed DRI elements to form virtual analysis platforms and
pipelines all impede world-class computational research in the UK.

## Objectives

Large scale data movement is currently difficult for anyone other than
a few expert users and, even then, it often requires involvement from
system administrators. This proposal seeks to aid the federation of
sites requiring access to large-scale data, reducing the entry barrier
for users.  We will:

1. Demonstrate user-driven large-scale data movement. based on representative case studies.
2. Implement test deployments of data transfer tools at several research-computing sites and assess
the ability to exploit the full national JANET network capacity and performance.
3. Implement a proof-of-concept (PoC) for accessible (though non-trivial) bulk, data-movement tools to aid user-driven data movement
4. Provide guidance related to data movement around the UK, and to/from UK sites from/to overseas
5. Provide data transfer tests and repeatable benchmarks for data movement utilising the PoC.
6. Compare four transfer technologies: optimised Rsync, Rclone, Globus and RUCIO+FTS3
7. Investigate workflow integration with batch schedulers and private object storage (including the DiRAC StorJ private cloud storage)
8. Consider sustainability aspects, such as vendor lock-in (up-front and lifetime costs) and standards compliance.

## Community

We have selected four representative, topical, data-intensive case
studies, which will place significant demands on DRI in coming years,
and provide excellent examples to inspire the wider
computational-science community. These use cases highlight practical
considerations, including high-bandwidth and low-latency data access,
large-scale data analysis, and long-term data value; as well as
good-practice considerations, including multinational collaboration,
access-control, researcher-led campaign development, and
community-scale engagement.

The case studies are:

1. LSST:UK - transfer of telescope data and events for UK-led processing and scientific analysis
2. DiRAC - transfer of large cosmology simulation datasets from production to analysis sites
3. UK SKA Regional Centre - data movement into and around the UK of multi-TB scale datasets
4. UKAEA - transatlantic transfer of simulated, fusion data for UK-based analysis and processing

These case studies have workflow requirements which involve complex
data handling. We will factor in these requirements when devising
potential solutions and recommendations: we will identify necessary
capabilities for data-hosting sites to ensure that user-led transfers
are efficient. We will provide training materials in data transfer,
and aim to offer a data transfer workshop at the HPC Days 2026
conference.

## More information

For more information please see the individual [work packages](workpackages.md)

