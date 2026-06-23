# Rclone

Rclone is widely used for data transfer to object storage such as S3. However it also supports a wide variety of other protocols, including SFTP and simple local file systems. It supports parallel transfers out-of-the-box which can help performance.

## Rclone tests on ARCHER2

We tested using rclone to transfer data between ARCHER2 and COSMA. As the time available was limited, a relatively small dataset of 10x10GB was used for these tests. Before any data could be copied, it was first necessary to install rclone, as it is not installed as standard on ARCHER2 (or most other HPC services). However, it is straightforward to download a binary package and run it as a non-privileged user:

```
wget https://downloads.rclone.org/v1.74.3/rclone-v1.74.3-linux-amd64.zip
unzip rclone-v1.74.3-linux-amd64.zip
cd rclone-v1.74.3-linux-amd64
```

It was then necessary to add COSMA as a "remote" (the term rclone uses for a remote system that it can connect to and transfer data to and from) and configure it. This was relatively straightforward as rclone implements an interactive interface that prompts for each necessary piece of information and provides reasonable defaults for most of them:

```
./rclone config
```

It was then possible to use rclone to copy data to and from COSMA using the SFTP protocol (the `--progress` option is not required but is desirable when copying large amounts of data as it gives regular updates on the transfer progress):

```
rclone --progress copy localdirectory COSMA:remotedirectory
```

However, this proved to be unreliable, with the transfers often stalling after a while. This turned out to be because rclone's default setting is to transfer 4 files simultaneously, and this appeared to be running into some kind of connection limit at the Durham end. By changing the setting to transfer only one file at a time, the data could be copied reliably, albeit more slowly:

```
rclone --progress --transfers 1 copy localdirectory COSMA:remotedirectory
```

We performed two transfers in each direction. Performance is shown in the table below:

| Source | Destination | Bandwidth (MB/s) |
| --- | --- | --- |
| ARCHER2 | COSMA | 98.9 |
| COSMA | ARCHER2 | 219.3 |
| ARCHER2 | COSMA | 97.5 |
| COSMA | ARCHER2 | 217.4 |

The data transfer was noticeably faster from Durham to Edinburgh than in the other direction. Overall, these numbers were very slow compared to those observed with Globus and rsync, but this may have been due to the relatively small data size.

Unfortunately we were not able to get rclone to work at any of the other sites during the time available. This was because the other sites require two factor authentication to log in via SSH, while COSMA only requires an SSH key and a password. It appears to be a limitation of rclone that it does not currently support 2FA as a Google search revealed that several other people had experienced the same problem and there was no obvious solution available. I attempted to work around this by logging into the remote site from the client site via SSH before initiating the transfer (sometimes only one TOTP code is required per day and subsequent logins from the same source are allowed to proceed without a code) but this resulted in the same error.

In summary:

- rclone supports a wide range of storage systems, protocols and features.
- It has out-of-the-box support for parallel transfers which can improve performance, however this can also be problematic as the default setting can trigger connection limits at some sites.
- It will usually be necessary for users to install and configure rclone themselves, however this is usually not too difficult.
- rclone's lack of support for 2FA over SFTP could be a severe limitation as many sites now require this.
