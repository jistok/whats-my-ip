# Cross-cloud solution to needing to know what your VM's IP address is to the external world

## To run in Cloud Foundry

```
cf push
...
requested state: started
instances: 1/1
usage: 128M x 1 instances
urls: whats-my-ip.apps.somedomain.io
last uploaded: Wed Nov 8 21:15:33 UTC 2017
stack: cflinuxfs2
buildpack: python_buildpack

     state     since                    cpu    memory      disk      details
#0   running   2017-11-08 04:16:12 PM   0.0%   0 of 128M   0 of 1G
```

## Get your IP

* Note the value in the `urls:` field of that output (above)
* Get your IP:

```
[me@myvm ~]$ ip=$( curl -s http://whats-my-ip.apps.somedomain.io )
[me@myvm ~]$ echo $ip
23.32.68.251
```

That's it.

