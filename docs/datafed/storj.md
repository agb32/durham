# Using StorJ

After logging into the StorJ satellite, you can select a project and create a bucket (or several).  You can then create an access key, which will give the shared credentials.

Put these shared credentials, in the format accesskey:secretkey in a file with permissions 600, e.g. .passwd-s3fs-datafed

To mount this, you can then use:

```
s3fs bucketname mnt/ -o passwd_file=.passwd-s3fs-datafed -o url=https://gateway-mt.storj.cosma.dur.ac.uk
```

For read-only buckets, ensure that the access key created only has read and list permissions. e.g. .passwd-s3fs-datafed-ro

There can be problems with permissions, so adding the `-o umask=0022` option to the s3fs line can solve this.


