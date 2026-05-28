# Globus

Globus is widely used by HPC systems to transfer data between systems.

We have a UK-based Globus user/admin mailing list (JISCMAIL) - please let Alastair know if you would like adding to this.

It has a concept of a [research data portal](https://docs.globus.org/guides/recipes/modern-research-data-portal/) which is a design pattern for providing secure and high performance access to research data.

## Transfer rates

| | Durham | Edinburgh | Cambridge | JASMIN | JISC |
| --- | --- | --- | --- | --- | --- |
| Durham | | [970MB/s](#cosma-archer2-transfer-tests) | [1360MB/s](#cosma-csd3-transfer-tests) | [386MB/s](#jasmin-transfer-tests) | [462MB/s](#jisc-transfer-tests) |
| Edinburgh | [994MB/s](#cosma-archer2-transfer-tests) | | [1810MB/s](#csd3-archer2-transfer-tests) | [876MB/s](#jasmin-transfer-tests) | [1090MB/s](#jisc-transfer-tests) |
| Cambridge | [751MB/s](#cosma-csd3-transfer-tests) | [2220MB/s](#csd3-archer2-transfer-tests) | | [819MB/s](#jasmin-transfer-tests) | [712MB/s](#jisc-transfer-tests) |
| JASMIN | [453MB/s](#jasmin-transfer-tests) | [617MB/s](#jasmin-transfer-tests) | [622MB/s](#jasmin-transfer-tests) | | |

(from location in column to location in row)

## Parallelism

Globus can perform data transfers in parallel, both in terms of transferring multiple files simultaneously (concurrency), and in terms of transferring multiple data streams within a file (parallelism). The table below shows the concurrency (first number) and parallelism (second number) that we observed between our sites. Note that these numbers are not shown in the transfer overview in the Globus web application, however they can be found by looking at the earliest event in the event log for a transfer.

| | Durham | Edinburgh | Cambridge | JASMIN | JISC |
| --- | --- | --- | --- | --- | --- |
| Durham | | 4, 8 | 2, 4 | 4, 4 | 2, 4 |
| Edinburgh | 4, 8 | | 4, 8 | 20, 8 | 4, 8 |
| Cambridge | 2, 4 | 4, 8 | | 4, 4 | 2, 4 |
| JASMIN | 4, 4 | 20, 8 | 4, 4 | | |

During our parallelism tests the parallelism and concurrency always remained consistent between each pair of sites across repeated transfers, and were also the same in both directions. However, this behaviour is not necessarily guaranteed.

Sites with a paid Globus licence can configure their own settings for preferred and maximum concurrency and parallelism; sites with a free licence are restricted to the default settings, which are shown below.

| Setting | Default value |
| --- | --- |
| Maximum concurrency | Number of servers * 4 |
| Preferred concurrency | Number of servers * 2 |
| Maximum parallelism | 8 |
| Preferred parallelism | 4 |

## Subscriptions

Globus offers a free subscription tier for limited control of data transfer.  However, higher performance transfers are available with a paid subscription.

There is potentially some issues related to commercial companies having University accounts (e.g. spin-offs and close collaborators) who would then have access to Globus through a University subscription.  The details here need to be ascertained.  Similarly, how the transfer of data to commercial partners can be managed needs to be determined.

### Globus availability on UK HPC facilities

The table below shows the availability of Globus at major HPC providers in the UK, as determined from public information such as documentation and the presence of discoverable Globus endpoints. This table represents the best of our knowledge at the present time but may not be completely correct or comprehensive.

| HPC facility | Globus available | Paid subscription | Parallelism configured |
| --- | --- | --- | --- |
| ARCHER2 (EPCC) | Yes | Standard | Yes |
| Cirrus (EPCC) | Yes | Standard | Yes |
| Tursa (DiRAC) | Yes | Standard | Yes |
| Baskerville (Birmingham) | Yes | Standard | Yes |
| UCL RDSS | Yes | Standard | Yes |
| University of York | Yes | High assurance | No |
| Apocrita (QMUL) | Yes | Standard | No |
| COSMA (Durham) | Yes | No | No |
| CSD3 (Cambridge) | Yes | Standard | No |
| JASMIN (RAL) | Yes | Standard | No |
| Isambard (GW4) | No | n/a | n/a |
| Sulis (HPC Midlands) | No | n/a | n/a |
| JADE (Oxford) | No | n/a | n/a |
| MMM | No | n/a | n/a |
| NI-HPC | No | n/a | n/a |
| Bede (EPSRC) | No | n/a | n/a |

Some sites have a paid Globus licence but do not appear to have configured the parallel transfer settings for their endpoint (using the `Maximum Concurrency`, `Preferred Concurrency`, `Maximum Parallelism` and `Preferred Parallelism` settings). This is denoted by a "No" in the right hand column of the table.

## COSMA/ARCHER2 Transfer Tests

In late October and early November 2025, various data transfer tests were performed between COSMA in Durham and ARCHER2 in Edinburgh, using Globus. System administrators in Edinburgh planned to enable MTU 9000 (so-called "Jumbo" ethernet frames) and were interested to see whether this would make a difference to the observed transfer rates in and out of the site. Durham, which already had jumbo frames enabled, was identified as a good candidate for testing and this also fitted well with the data federation project's goal of investigating different data transfer technologies.

Set up was straightforward as both COSMA and ARCHER2 were already registered as Globus endpoints. Before the first use of these endpoints it was necessary to perform an authorisation step, and for COSMA it was also necessary to submit a ticket to the COSMA helpdesk asking for the desired directory to be added to the list of directories visible to Globus. As there was no suitable test data available at either site, random data files were generated by using the `dd` utility to copy random data from `/dev/urandom`. Using random data ensures that the files will not be compressible so that the reported transfer rates will be accurate.

The table below shows the data transfers performed and the transfer rates achieved:

| Date/time | Source | Destination | Number of files | Size of each file (GB) | Transfer rate (MB/s) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| MTU 1500 
| 29/10/2025 11:50 | COSMA | ARCHER2 | 50 | 100 | 815.08 |
| 31/10/2025 22:05 | ARCHER2 | COSMA | 50 | 100 | 916.13 |
| 05/11/2025 07:40 | COSMA | ARCHER2 | 500 | 10 | 970.24 |
| 05/11/2025 12:44 | ARCHER2 | COSMA | 500 | 10 | 994.09 |
| MTU 9000
| 12/11/2025 09:45 | COSMA | ARCHER2 | 500 | 10 | 914.34 |
| 12/11/2025 11:23 | ARCHER2 | COSMA | 500 | 10 | 944.99 |
| 13/11/2025 07:08 | COSMA | ARCHER2 | 50 | 100 | 860.15 |
| 13/11/2025 09:29 | ARCHER2 | COSMA | 50 | 100 | 817.52 |

The first four transfers were performed before MTU 9000 was enabled at Edinburgh, the last four after. There was no obvious performance improvement from this configuration change, with the transfers both before and after running at similar speeds in the range 800-1000MB/s. It is likely that other bottlenecks in the network were more significant than this setting.

Transfers from ARCHER2 to COSMA were generally slightly faster than those in the other direction, though given the relatively small number of transfers performed, this may have just been coincidence. Surprisingly the transfers of 500 smaller files were noticeably faster than those of 50 larger files; this may relate to how Globus handles transfers internally. Possibly the larger number of files offers more opportunity for parallelism.

## CSD3/ARCHER2 Transfer Tests

We were interested in testing transfer speeds between ARCHER2 and another site in addition to Durham: as Durham does not have a paid Globus licence, we speculated that this may be restricting the transfer performance. CSD3 at Cambridge was selected for this as, like Edinburgh, it does have a paid Globus licence.

Setting up authentication for the Cambridge endpoint was a slightly different process from that at Edinburgh and Durham. First it was necessary to notify the local system administrator, Paul Browne, who granted access to Globus to my CSD3 user account. The next step was to create a Globus ID (a distinct entity from a Globus user account) and use this to authenticate with the Cambridge endpoint. While both Edinburgh and Durham handle Globus authentication through their normal user registration systems, Cambridge uses the Globus ID as an intermediary. However, this was straightforward - the email address associated with my Globus ID was matched to the one registered with my CSD3 user account and I was immediately able to access my files via Globus.

Several transfer tests were then performed, as shown in the table below. Note that the number of files and the total volume of data used here were less than for the COSMA/ARCHER2 tests; this was due to more restrictive disk quotas at Cambridge.

| Date/time | Source | Destination | Number of files | Size of each file (GB) | Transfer rate (MB/s) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 15/01/2026 11:06 | ARCHER2 | CSD3 | 50 | 10 | 1008.00 |
| 15/01/2026 11:15 | CSD3 | ARCHER2 | 50 | 10 | 825.12 |
| 15/01/2026 11:30 | ARCHER2 | CSD3 | 50 | 10 | 855.07 |
| 15/01/2026 11:43 | CSD3 | ARCHER2 | 50 | 10 | 551.52 |

There was no obvious improvement in transfer rate over the previous Edinburgh/Durham transfers. For the Edinburgh/Cambridge tests the transfer rates seemed more variable, perhaps due to the greater distance between Edinburgh and Cambridge. Overall the rates were about the same as between Edinburgh and Durham, which could suggest the speed is limited by something at or near the Edinburgh end of the link.

### Further Tests after CSD3 Upgrade

A few weeks after our initial transfer tests, the CSD3 Globus endpoint was upgraded to a paid Globus licence with mandatory encryption enabled. After this change we ran additional tests to check if the transfer rates had improved.

| Date/time | Source | Destination | Number of files | Size of each file (GB) | Transfer rate (MB/s) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 23/02/2026 11:39 | CSD3 | ARCHER2 | 50 | 10 | 1810.00 |
| 23/02/2026 11:46 | ARCHER2 | CSD3 | 50 | 10 | 2220.00 |
| 23/02/2026 11:52 | CSD3 | ARCHER2 | 50 | 10 | 1810.00 |
| 23/02/2026 12:04 | ARCHER2 | CSD3 | 50 | 10 | 2160.00 |

The observed transfer rates had improved significantly, having roughly doubled from their original values. In addition, the rates also appeared to be more consistent than before, although this may have been down to transient factors such as network usage.

## COSMA/CSD3 Transfer Tests

For completeness, we also tested transfer rates between COSMA and CSD3. As for the CSD3/ARCHER2 tests, the volume of data transferred was restricted by the disk space available at Cambridge.

| Date/time | Source | Destination | Number of files | Size of each file (GB) | Transfer rate (MB/s) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 26/01/2026 10:13 | CSD3 | COSMA | 50 | 10 | 599.50 |
| 26/01/2026 10:31 | COSMA | CSD3 | 50 | 10 | 670.34 |
| 26/01/2026 10:52 | CSD3 | COSMA | 50 | 10 | 571.67 |
| 26/01/2026 11:11 | COSMA | CSD3 | 50 | 10 | 693.73 |

This time the transfer rate was noticeably slower than the previous tests between Edinburgh and Durham or Cambridge. This could be due to the fact that Durham has a slower network link than Edinburgh, as well as not having a paid Globus licence. In addition, transfers from Durham to Cambridge were faster than those in the opposite direction, though given that only two tests were run in each direction, this may have just been coincidence.

### Further Tests after Cambridge Upgrade

After Globus was upgraded at Cambridge, we also reran our tests between COSMA and CSD3. While we did not expect the results to have improved as much as the ARCHER2 to CSD3 results due to the lack of paid Globus licence at Durham, we were still interested to see if there was any change.

| Date/time | Source | Destination | Number of files | Size of each file (GB) | Transfer rate (MB/s) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 23/02/2026 10:50 | CSD3 | COSMA | 50 | 10 | 750.08 |
| 23/02/2026 11:05 | COSMA | CSD3 | 50 | 10 | 1340.00 |
| 23/02/2026 11:14 | CSD3 | COSMA | 50 | 10 | 751.00 |
| 23/02/2026 11:28 | COSMA | CSD3 | 50 | 10 | 1360.00 |

Interestingly, a significant improvement was again observed, particularly in the Durham to Cambridge direction which saw transfer speeds roughly double relative to the previous tests. As with the tests between Edinburgh and Cambridge, these transfer times appeared to be more consistent across multiple tests than the earlier ones.

## JASMIN Transfer Tests

After gaining access to the STFC's JASMIN system at RAL, we ran Globus transfer tests between here and Durham, Cambridge and Edinburgh. Due to restricted disk space quota on JASMIN a smaller dataset (9x10GB files) was used for these tests.

| Source | Destination | Transfer rate (MB/s) |
| --- | --- | --- |
| COSMA | JASMIN | 255.0 |
| JASMIN | COSMA | 385.7 |
| COSMA | JASMIN | 452.8 |
| JASMIN | COSMA | 128.9 |
| COSMA | JASMIN | 195.7 |
| JASMIN | CSD3 | 288.3 |
| CSD3 | JASMIN | 265.9 |
| JASMIN | CSD3 | 819.4 |
| CSD3 | JASMIN | 621.6 |
| JASMIN | ARCHER2 | 837.7 |
| ARCHER2 | JASMIN | 617.3 |
| JASMIN | ARCHER2 | 875.5 |
| ARCHER2 | JASMIN | 503.6 |

Despite the smaller dataset, the transfer rates were broadly similar to those observed in our other tests. However there does appear to be a wider variability between the performance of individual test runs than we have seen in other tests which could indicate that the shorter running transfers are more sensitive to network conditions.

## Scale tests

After observing that [rsync](rsync.md) appears to perform more poorly with smaller data sizes, we tested Globus with the smaller 90GB dataset between our three core sites.

| Source | Destination | Transfer rate (MB/s) |
| --- | --- | --- |
| ARCHER2 | COSMA | 522.7 |
| COSMA | ARCHER2 | 752.9 |
| ARCHER2 | COSMA | 531.3 |
| COSMA | ARCHER2 | 771.6 |
| ARCHER2 | CSD3 | 1190 |
| CSD3 | ARCHER2 | 1050 |
| ARCHER2 | CSD3 | 1490 |
| CSD3 | ARCHER2 | 1080 |
| COSMA | CSD3 | 1000 |
| CSD3 | COSMA | 431.5 |
| COSMA | CSD3 | 953.6 |
| CSD3 | COSMA | 469.1 |

From these results, Globus's performance appears to be less affected by the dataset size than rsync's. Although some of the tests do show a lower throughput compared to the large 5TB tests, the difference is much less than the factor of 5-10 observed with rsync.

## JISC transfer tests

After JISC made some of our test datasets available via Globus, we ran several tests between JISC and our other sites. Note that these tests were unidirectional as we did not have write access to JISC, and also that JISC to JASMIN was not tested due to lack of disk quota on JASMIN.

| Source | Destination | Dataset | Transfer rate (MB/s) |
| --- | --- | --- | --- |
| JISC | COSMA | 50x10GB | 461.6 |
| JISC | COSMA | 50x100GB | 389.4 |
| JISC | COSMA | 1000x1GB | 341.4 |
| JISC | COSMA | 50x10GB | 360.3 |
| JISC | COSMA | 50x100GB | 336.1 |
| JISC | COSMA | 1000x1GB | 377.0 |
| JISC | CSD3 | 50x10GB | 684.7 |
| JISC | CSD3 | 50x100GB | 569.8 |
| JISC | CSD3 | 1000x1GB | 696.4 |
| JISC | CSD3 | 50x10GB | 711.8 |
| JISC | CSD3 | 50x100GB | 551.7 |
| JISC | CSD3 | 1000x1GB | 676.1 |
| JISC | ARCHER2 | 50x10GB | 972.8 |
| JISC | ARCHER2 | 50x100GB | 838.9 |
| JISC | ARCHER2 | 1000x1GB | 1060 |
| JISC | ARCHER2 | 50x10GB | 1030 |
| JISC | ARCHER2 | 50x100GB | 829.5 |
| JISC | ARCHER2 | 1000x1GB | 1090 |

Transfer rates were in the same range as those already observed between the other sites. Notably, and slightly surprisingly, the largest dataset (50x100GB files) was generally slightly slower to transfer than the two smaller datasets, although in most cases the speed difference was relatively small.

## Globus Command Line Interface Usage

Globus transfers can be initiated and monitored through the Globus web interface available at [https://app.globus.org](https://app.globus.org). However, for some use cases (particularly when scripting and automation are desired), the command line interface may be more suitable. This can easily be installed through `pip`:

```
pip install globus-cli
```

Once installed, it is necessary to log in to the Globus service before transfers can be managed. To do this, run:

```
globus login
```

This will direct you to a URL on the Globus website where you can authenticate with Globus and grant permission for the command line client to access your account.

In order to interact with Globus endpoints, it is necessary to have their UUIDs. These can be found via the Globus web interface by searching for the endpoint, clicking on the three dots to the right of its name, and copying the UUID from the bottom of the "Overview" tab that appears. For example, the ARCHER2 endpoint's UUID is `3e90d018-0d05-461a-bbaf-aab605283d21` and COSMA's is `25e7309e-82ed-11e9-bf4e-0e4a062367b8`. It is also possible to find endpoints directly from the CLI using the `globus endpoint search` command.

It may be convenient to store the UUIDs you are working with in environment variables to avoid having to copy and paste them and to make it clear which endpoint subsequent commands are referring to:

```
export GLOBUS_ENDPOINT_ARCHER2=3e90d018-0d05-461a-bbaf-aab605283d21
export GLOBUS_ENDPOINT_COSMA=25e7309e-82ed-11e9-bf4e-0e4a062367b8
```

Once you are logged in and have the endpoint IDs, you can list files available on the endpoint, or in a certain subdirectory of the endpoint:

```
globus ls $GLOBUS_ENDPOINT_ARCHER2
globus ls $GLOBUS_ENDPOINT_ARCHER2:/mnt/lustre/a2fs-nvme/work/z19/z19/jamesp-z19/globus/
```

To initiate a transfer between two endpoints, use the `globus transfer` command. For example, the command below will initiate a transfer of a file called `test1` from ARCHER2 to COSMA:

```
globus transfer $GLOBUS_ENDPOINT_ARCHER2:/mnt/lustre/a2fs-nvme/work/z19/z19/jamesp-z19/globus/test1 $GLOBUS_ENDPOINT_COSMA:/cosma7/data/ip005/dc-perr3/globus/test1
```

You can check the status of all your current Globus operations by running:

```
globus task list
```

This will show a summary table with the most recent tasks at the top. The first column gives the task ID for each task. You can use this ID to request more detailed information about an individual task:

```
globus task show f2dc4951-d1df-11f0-bb8c-0221bf474485
```

These commands are sufficient for initiating transfers and monitoring their progress. However, many other commands are available for more advanced tasks, and these are detailed in the [Globus documentation](https://docs.globus.org/cli/).
