# Data Federation Workshop

18-19th May 2026

*Location:* Institute for Computational Cosmology, Durham University
 - Room OCW017, Ogden Centre West building, South Road, DH1 3LE
 - [Google maps location](https://www.google.com/maps/place/54%C2%B046'01.8%22N+1%C2%B034'29.4%22W/@54.76718,-1.5797085,17z){:target="_blank"}

![Location](../images/ocwBuilding.png)

Investigation of large scale data movement and a Globus-focused session.

The afternoon of 18th will focus on the Globus suite of tools, including configuration, installation and usage, and overview of features.

The morning of 19th will focus on user-driven large scale data transfer.

We welcome talks on this topic - please provide details in the [registration form](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=i9hQcmhLKUW-RNWaLYpvlKHkTxd26sdLkOaQl2zCEXpUQTlENlBGVklTSks4WUVSOU1SMVBIRUc4RC4u){:target="_blank"}.

This workshop is funded by the Data Federation project which is part of [NFCS+](https://nfcs-networkplus.ac.uk/){:target="_blank"}.

We are also setting up a UK Globus users JISCMAIL list - please let Alastair know if you would like to be added to this.

## Registration

Please [register here](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=i9hQcmhLKUW-RNWaLYpvlKHkTxd26sdLkOaQl2zCEXpUQTlENlBGVklTSks4WUVSOU1SMVBIRUc4RC4u){:target="_blank"}.

Registration will close on 10th May, though obviously it would be helpful to sign up earlier!  Abstracts for talks are due by 1st May.

## Agenda

Monday 18th

- 12:30 Arrival and lunch
- 13:30 Globus workshop
  - Including features, installation and configuration
- 15:00 Refreshment break
- 15:30 Globus compute, flows, data streaming
  - A more indepth look at the Globus family of tools
- 17:00 Close
- 19:00 Dinner

Tuesday 19th

- 09:00 Arrival and refreshments
- 09:15 Welcome
- 09:20 Data sharing at the Vera C Rubin Telescope (LSST), George Beckett
- 09:40 [Globus usage on JASMIN](#globus-usage-on-jasmin), Matt Pritchard
- 10:00 [Data transfer facilities on COSMA](#data-transfer-facilities-on-cosma), Alastair Basden
- 10:20 [Globus at the Rosalind Franklin Institute](#globus-at-the-rfi), Dimitrios Bellos
- 10:40 [Exploring Globus and rsync performance](#exploring-globus-and-rsync-performance), James Perry
- 11:00 Refreshments
- 11:30 JISC, Janet, network test facilities, perfSonar, Globus test, Tim Chown
- 11:50 Tuning and measuring network performance, Chris Walker
- 12:10 Discussion
- 12:30 Lunch
- 13:30 End of workshop

## Abstracts

### Globus usage on JASMIN

A talk on how we provide Globus services to users of JASMIN. From different perspectives:
- Service operator (our multi-DTN setup, how we use our own OIDC server, potential for multiple collections on same endpoint, how we monitor)
- User Support perspective (how access is provided, documentation, common queries)
- Known use cases (ad-hoc transfers, ARCHER2-JASMIN workflow, distributed lab instruments, large-scale replication)
- future plans, including
  - STFC subscription


### Data transfer facilities on COSMA

The COSMA HPC system, part of the DiRAC national facility, provides users with multiple options for data transfer.  Some of these are described here, including how users can optimise their workflows.  Several project-specific bespoke capabilities are also described.

### Globus at the RFI

The Rosalind Franklin Institute has been using Globus for 4 years to transfer high-resolution multimodal biological data from our instruments to our analysis platforms. Approximately Franklin is generating around 70 terabytes a month, which requires high speed and robust transfers. Distributed data transfer solutions, such as Globus facilitate this goal, and we aim to also use it in automated pipelines that do not require a human in the loop. Towards this goal, Rosalind Franklin Institute currently holds a Globus subscription and are using many of the cabilities that Globus offers.

Firstly, we have set up a Globus Connect Server (GCS) endpoint that is serviced by multiple Data Transfer Nodes (aka multiple machines) to increase both its robustness and how much network traffic it can handle. Our GCS endpoint services multiple collections, some utilize Globus' POSIX connector and others Globus' S3 connector. We also take advantage of the Globus' groups functionality to manage the access permissions in our S3 (guest) collections. This is because the S3 compatible object store we are using, Echo (1), does not allow to assign an owner either to the buckets or objects of an account. Thus Globus allowed us to implement fine grain access control of the object store, without having to provide any object store keys to our users, which could be detrimental if they accidentally get leaked.

Secondly, we have developed and released FlowCron (2) which is a Function-as-a-Service software tool that can facilitate users to access HPCs to process their data using a Globus Flow to accommodate any data transfers. This significantly reduces the time to science. 

Lastly, we released Rosalind Franklin Institute’s GlobusAPI (3). Our RFI-GlobusAPI container image provides an intuitive interface with Globus Python SDK, enabling the easy deployment of Globus microservices, which facilitates the incorporation of Globus within automated data processing pipelines. RFI-GlobusAPI offers multiple useful high in abstraction commands, and it has already been tested as part of ArgoWF workflows. Furthermore, RFI-GlobusAPI is open source and available to all. Our future goals include the expansion of RFI-GlobusAPI with further utility, allowing us to incorporate it into different parts of our data lifecycle to create a secure, scalable, reproducing and efficient automated data infrastructure that can provide FAIR (4,5) data for all our science.
 
1. https://www.sc.stfc.ac.uk/platforms-and-services/echo/
2. https://doi.org/10.12688/wellcomeopenres.23491.2
3. https://github.com/rosalindfranklininstitute/rfi-globus-api
4. https://doi.org/10.1038/sdata.2016.18
5. https://www.go-fair.org/fair-principles 

### Exploring Globus and rsync performance

As part of the NFCS Federated Data Movement project, we have been investigating data transfer technologies, including Globus and rsync, with the aim of providing guidance to users on which technologies might be suitable for their use cases. We tested Globus and rsync between 5 UK HPC sites looking at performance, ease-of-use and other relevant facctors. As part of this work we have also used iperf3 to investigate the bandwidth of the underlying network links, as well as exploring how variations in data size affect transfer speeds.

## Directions

The workshop is a pleasant 25-30 minute walk along the river bank from the train station.

For those coming by car, park at your nearest station and catch a train!

## Hotels

There are many hotels in Durham.
