# Versitygw: Exporting HPC file systems as S3

[Versitygw](https://github.com/versity/versitygw) is an open source tool which can be used to export a file system as S3.

## Instructions

The steps (with further details below) are:

1. Download and compile following the tool instructions
2. Select a host with an accessible port (or via a ssh tunnel)
3. `ROOT_ACCESS_KEY="testuser" ROOT_SECRET_KEY="mysecret" ./versitygw --port :10000 posix /path/to/my/subdir`
4. Access the data using e.g. aws, rclone, etc

### Notes

#### Step 2:

When selecting a host (e.g. a login node), you will need a port that is not firewalled, and not in use by something else.  This is likely to be difficult to achieve, and may require contacting technical support (who will then be curious about security).  Alternatively, if you have your own host with accessible ports, you can set up an ssh tunnel.  However, this is not optimal, as all data will then traverse your own host.

To set up an ssh tunnel, you could use e.g. `ssh -L 8000:localhost:PORT USER@LOGINNODE` where the LOGINNODE is the node on which you run versitygw, and PORT is the port you select (10000 in the above example).  This will forward port 8000 on your local system to port 10000 on the login node (which we assume is inaccessible due to a firewall).

#### Step 3:

The access key and secret key that you select are what you will give to the tool seeking to access the data.  You should probably keep these secret.

The --readonly flag means that clients cannot modify the bucket (portion of the directory structure) that you expose.

Within subdir, you should have a directories starting with a lowercase letter. 

For this to work, you need the `user_xattr` flag set on the file system, typically as an option in /etc/fstab.

#### Step 4: accessing the data

There are multiple tools you can use to access the data.

##### aws

Example of usage:

`aws --endpoint-url http://172.17.100.11:10000 configure list`

Creating a bucket (for end points with write access): `aws --endpoint-url http://172.17.100.11:10000 s3 mb s3://testbucket --region us-east-1`

Copying to a bucket (write access required): `aws --endpoint-url http://172.17.100.11:10000 s3 cp  tmp.tex s3://testbucket/ --region us-east-1`

Reading from a bucket: `aws --endpoint-url http://172.17.100.11:10000 s3 cp   s3://testbucket/tmp.tex mytmp.tex --region us-east-1`

##### rclone

To configure rclone, you should use options similar to:

```
rclone config
n) Net remote
name> my-versity-export
Storage> 5   (S3 compatible)
provider> 24  (Other)
env_auth> 1  (enter credentials at next step)
access_key_id> my_access_key
secret_access_key> my_secret_key
region>     (leave empty)
endpoint> http://MYIPADDRESS:PORT
location_constraint>  (leave empty)
acl> 2   (allusers group get read access)
```

Then save it.

And to use it:

`rclone lsf my-versity-export:`

and verious other rclone commands.

# Flamingo tests

Set up using e.g. `ROOT_ACCESS_KEY="f" ROOT_SECRET_KEY="f" ./versitygw --port :50011 posix /cosma7/data/Eagle/DataRelease/L0100N1504/PE/REFERENCE`

Note: S3 requires bucket names to all be lowercase and cannot contain underscore characters.  If directories have capital letters in the names, they can all be placed into a single directory, and that used.

After appropriate config, `rclone lsf versity-dataweb-50011:` can be used to list.


## Mounting on a client

The s3fs fusemount command can be used.  To do this, you can e.g.:

```
echo f:f > .passwd-s3fs
mkdir mnt
s3fs data mnt/ -o passwd_file=.passwd-s3fs -o url=http://193.60.196.24:50011 -o use_path_request_style
```

### Testing partial download

During testing of partial download tests, the `file` command was used on a 263MB file on a 20Mbit/s home broadband connection.  The result was returned in 29 seconds, which would equal 70Mbit/s download speed if the whole file was transferred - therefore, only parts of the file were transferred, demonstrating the "zero-copy" data transfer.



