# Rsync

Rsync is a standard tool for data transfer, and widely used for small volumes of data.



## Transfer rates


| | Durham | Edinburgh |
| --- | --- | --- |
| Durham | | 80Mbps |
| Edinburgh | | |

## Transfer details and parameters

### Durham to TURSA (Edinburgh)

The command used is:

```
echo TOTP_CODE | rsync -av -e "ssh -i /path/to/ssh/key" tmp.tar TURSAUSER@tursa.dirac.ed.ac.uk:
```

From login0a (with a 100Mbps connection):

sent 986,506,495 bytes  received 35 bytes  73,074,557.78 bytes/sec
total size is 986,265,600  speedup is 1.00

From dataweb (40Gbps connectivity with bonded 4x 10G links over JANET):

sent 986,506,495 bytes  received 35 bytes  78,920,522.40 bytes/sec
total size is 986,265,600  speedup is 1.00
