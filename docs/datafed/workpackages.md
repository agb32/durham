# Work packages

## WP!: Requirements capture and landscape review

We will perform a landscape review of requirements from widely
different communities (e.g., Royce Institute, Rosalind Franklin
Institute, MRC, institutional repositories) who are or could be
interested in making use of a federated infrastructure; and record the
best practices being pursued in federated research infrastructures
globally including in person discussions with these organisations. We
will work with these facilities to ensure the survey is applicable to
a wide range of sciences before embarking on dissemination to the
wider community.

In parallel we will perform a paper-based technology evaluation,
defining preliminary requirements (from partners and their
collaborators) and assess which technologies meet these requirements,
along with current best practice. Requirements will cover aspects like
ease of use and installation, cost, security, performance and
longevity. Access control and accounting capabilities will also be
considered, including compatibility with TREs. This review will also
explicitly cover capabilities (particularly non-free additions)
offered by Globus, Rucio+FTS, Rsync and Rclone.

### Deliverables

1. Outcomes of user survey and technology review
2. Best practices from other DRIs
3. Report into technology capabilities

## WP2: Technology benchmarks

We will install and configure several different transfer technologies
for practical evaluation. While we have selected only a subset of the
available technologies, the methods developed will be applicable as
new technologies come to market. Once installed, testing of data
transfer performance (e.g., large-file and many-file) will be carried
out between sites, with configuration changes investigated. The
following technologies will be installed:

- FTS3 client (Xrootd and https protocols): COSMA and Somerville.
- RUCIO: COSMA. This scientific data management solution will be used to enable
policy-driven workflows and data movement.
- Globus: DIaL, RAL, UKAEA, Somerville. Globus is a widely used technology for bulk data
transfer, with potential for integration with compute and for data publishing,
- Rclone: COSMA, EPCC, DIaL. Data management on cloud storage.
- S3: UKAEA. To access data from HPC/IRIS sites with S3 endpoints, including DiRAC StorJ.

Security tests will be performed following Jisc documentation around
Science DMZ. Jisc is exploring establishing best practices in science
DMZ deployment and appropriate security policy implementation and
assessment, and we will follow these guidelines. UKAEA will run
pentests.

### Deliverables

1. Report of Performance Tuning and Testing including a "Lessons Learned" to
support any future adoption.
2. Report of Security Assessment of different protocols.

## WP3: Use cases

We will prove data transfer based on requirements from the identified use cases, using the
technologies being evaluated.

- LSST: Demonstrate pulling astronomy science products into COSMA from Somerville
- DiRAC: Optimise bulk data transfers between DiRAC sites, including to archival tape storage.
- UKSRC: Replication of data transfer challenges between UK sites, without operator involvement.
- UKAEA: US to UK transfers at multiple sites using multiple technologies, and S3 transfers using cloud-optimised zarr format, relevant for AI models.

### Deliverables

1. LSST report
2. DiRAC report
3. UKSRC report
4. UKAEA report

## Timescales

- 2M: Installation of Globus and Rclone completed.
- 3M: User survey and technology review completed.
- 3M: Technology capabilities report delivered.
- 6M: Performance testing of Globus, Rclone and Rsync completed.
- 7M: Data access from cloud end-points characterised.
- 8M: Installation of Rucio+FTS3 completed.
- 9M: PoC demonstration of user-driven data transfer case studies demonstrated.
- 10M: Performance testing completed and report delivered.
