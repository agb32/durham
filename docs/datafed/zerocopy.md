# Zero-copy data transfer

How to access data without pre-staging?

Often when processing large datasets, the data is pre-staged from the storage or repository, onto scratch storage of the compute system upon which it will be processed.  For large datasets, this can take many weeks or months.

However, if only a subset of this data is required, and perhaps not known in advance, it is possible to access the data remotely, transferring only the required bytes across the network.

There are various ways of doing this.  Here we consider how file systems can be remotely exported by users from large-scale computing facilities.

## S3 object export

S3 has become a standard for object storage.  It is possible to export local POSIX file systems (e.g. Lustre) as S3 objects, which can then be accessed from elsewhere.  There are several tools that will facilitate this:

- [versitygw](versitygw.md)

