<!--  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax   -->
# Devopslive10 -Assignment 1
## Part 2

Step1: Pick Docker  
   

Step 2: Run Docker

```
root@dice-devops:/home# docker run -p 8000:8000  -d -t --name latest_unicorn    unicorn:v1
1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c
root@dice-devops:/home# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS        PORTS                                       NAMES
1c421046eb02   unicorn:v1   "python3 main.py"        2 seconds ago   Up 1 second   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   latest_unicorn
8b121467c308   nginx        "/docker-entrypoint.…"   13 hours ago    Up 13 hours                                               pedantic_nash
3ea6aa7e4382   nginx        "/docker-entrypoint.…"   39 hours ago    Up 39 hours   80/tcp                                      blissful_shtern

```

![image](https://github.com/sydali/devopslive1.2/assets/449393/53b1fe0f-db9f-486c-84a4-d57fa4b53b2f)





Step 3: Docker Commands


```
root@dice-devops:/home/Repos/devopslive1.1# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED        STATUS        PORTS                                       NAMES
1c421046eb02   unicorn:v1   "python3 main.py"        4 hours ago    Up 4 hours    0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   latest_unicorn
8b121467c308   nginx        "/docker-entrypoint.…"   17 hours ago   Up 17 hours                                               pedantic_nash
3ea6aa7e4382   nginx        "/docker-entrypoint.…"   42 hours ago   Up 42 hours   80/tcp                                      blissful_shtern
root@dice-devops:/home/Repos/devopslive1.1# docker stop 1c421046eb02
1c421046eb02
root@dice-devops:/home/Repos/devopslive1.1# docker logs 1c421046eb02
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     103.85.36.175:59353 - "GET / HTTP/1.1" 200 OK
INFO:     103.85.36.175:59353 - "GET / HTTP/1.1" 200 OK
INFO:     103.85.36.175:59267 - "GET /docs HTTP/1.1" 200 OK
INFO:     103.85.36.175:59267 - "GET /openapi.json HTTP/1.1" 200 OK
WARNING:  Invalid HTTP request received.
INFO:     45.56.86.210:44478 - "GET / HTTP/1.1" 200 OK
INFO:     65.49.20.77:12841 - "GET / HTTP/1.1" 200 OK
INFO:     65.49.20.113:58687 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     65.49.20.85:28783 - "GET http%3A//api.ipify.org/?format=json HTTP/1.1" 404 Not Found
INFO:     65.49.20.69:22323 - "CONNECT www.shadowserver.org%3A443 HTTP/1.1" 404 Not Found
WARNING:  Invalid HTTP request received.
INFO:     103.85.36.175:59363 - "GET / HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
root@dice-devops:/home/Repos/devopslive1.1# docker inspect 1c421046eb02
[
    {
        "Id": "1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c",
        "Created": "2023-11-10T01:00:25.13377702Z",
        "Path": "python3",
        "Args": [
            "main.py"
        ],
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-11-10T01:00:25.631697996Z",
            "FinishedAt": "2023-11-10T04:39:59.265518312Z"
        },
        "Image": "sha256:94d5dc12ddeaade77dde5d98982c79eb11ba8e83e044f843ec318aa9653773b2",
        "ResolvConfPath": "/var/lib/docker/containers/1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c/hostname",
        "HostsPath": "/var/lib/docker/containers/1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c/hosts",
        "LogPath": "/var/lib/docker/containers/1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c/1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c-json.log",
        "Name": "/latest_unicorn",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "8000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                72,
                254
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/cdbcdee499b955a8905f2465558ab830bf20ae8fad301fd86d12dd53fd8b23ad-init/diff:/var/lib/docker/overlay2/e875e8915b011ac1552749173d0115fb57ea9fe9a8a4321277cfbb6a5a82df56/diff:/var/lib/docker/overlay2/nlje56wiuqo6r05zf0cqvpbmv/diff:/var/lib/docker/overlay2/xu9p18ay142nofswhtjyy8n3m/diff:/var/lib/docker/overlay2/mgh8eroanks074w5ytnaupkf7/diff:/var/lib/docker/overlay2/fd801de856ab38e6d25842fd9eab86a16569aae28d10c8d2d7754eef316901c4/diff:/var/lib/docker/overlay2/5a8db79d67bea09af919332486b93467b3b56521afadfc6adaa1083375e2b836/diff:/var/lib/docker/overlay2/554245c86987bf8887cbe9556f036afaa6d19600d42bdc69c61208d3a90af323/diff:/var/lib/docker/overlay2/d2b244c2a33dece90d300fa16bfcb39ca52892f6c73eb61be8632746e3f6bba3/diff:/var/lib/docker/overlay2/8ab191dd746e79c37653a18f2cf8a14408c025ba52e322023c555979c2bfa3c9/diff:/var/lib/docker/overlay2/f8b4bf64158e3766086723d2c43331f5189b04273ea8d2d34ec1661aeeb5c216/diff:/var/lib/docker/overlay2/8f6da9b91783321e273ec740e4d9ff46364069c0c8b4a03cfece175171fa086a/diff:/var/lib/docker/overlay2/286841d4d97b44a876967c873ba86635ac0c30239040c8942b103188b2047eda/diff",
                "MergedDir": "/var/lib/docker/overlay2/cdbcdee499b955a8905f2465558ab830bf20ae8fad301fd86d12dd53fd8b23ad/merged",
                "UpperDir": "/var/lib/docker/overlay2/cdbcdee499b955a8905f2465558ab830bf20ae8fad301fd86d12dd53fd8b23ad/diff",
                "WorkDir": "/var/lib/docker/overlay2/cdbcdee499b955a8905f2465558ab830bf20ae8fad301fd86d12dd53fd8b23ad/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "1c421046eb02",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "8000/tcp": {}
            },
            "Tty": true,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
                "PYTHON_VERSION=3.8.18",
                "PYTHON_PIP_VERSION=23.0.1",
                "PYTHON_SETUPTOOLS_VERSION=57.5.0",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/c6add47b0abf67511cdfb4734771cbab403af062/public/get-pip.py",
                "PYTHON_GET_PIP_SHA256=22b849a10f86f5ddf7ce148ca2a31214504ee6c83ef626840fde6e5dcd809d11"
            ],
            "Cmd": null,
            "Image": "unicorn:v1",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "python3",
                "main.py"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "5e69e930dac7ebeee95770337afd8571bc8f2b58be114a91aa62852316521338",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/5e69e930dac7",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "67d53fdcca743bb98a9084b8d25849e749acb538a6fc6c5482cfa94641ae0317",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "",
                    "DriverOpts": null
                }
            }
        }
    }
]

docker stats latest_unicorn

CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT     MEM %     NET I/O     BLOCK I/O     PIDS
1c421046eb02   latest_unicorn   0.30%     39.28MiB / 969.4MiB   4.05%     866B / 0B   9.49MB / 0B   1


root@dice-devops:/home/Repos/devopslive1.1# docker top  latest_unicorn
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                401325              401302              0                   04:42               pts/0               00:00:01            python3 main.py
root@dice-devops:/home/Repos/devopslive1.1# dcoker pause latest_unicorn
Command 'dcoker' not found, did you mean:
  command 'docker' from snap docker (20.10.24)
  command 'docker' from deb docker.io (24.0.5-0ubuntu1~22.04.1)
  command 'docker' from deb podman-docker (3.4.4+ds1-1ubuntu1.22.04.2)
See 'snap info <snapname>' for additional versions.
root@dice-devops:/home/Repos/devopslive1.1# docker  pause latest_unicorn
latest_unicorn
root@dice-devops:/home/Repos/devopslive1.1# docker  unpause latest_unicorn
latest_unicorn
root@dice-devops:/home/Repos/devopslive1.1# docker rename latest_unicorn latest_unicorns
root@dice-devops:/home/Repos/devopslive1.1# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED        STATUS         PORTS                                       NAMES
1c421046eb02   unicorn:v1   "python3 main.py"        4 hours ago    Up 5 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   latest_unicorns
8b121467c308   nginx        "/docker-entrypoint.…"   17 hours ago   Up 17 hours                                                pedantic_nash
3ea6aa7e4382   nginx        "/docker-entrypoint.…"   42 hours ago   Up 42 hours    80/tcp                                      blissful_shtern
root@dice-devops:/home/Repos/devopslive1.1#


root@dice-devops:/home/Repos/devopslive1.1# docker stop latest_unicorns
latest_unicorns
root@dice-devops:/home/Repos/devopslive1.1# docker restart  latest_unicorns
latest_unicorns
root@dice-devops:/home/Repos/devopslive1.1# docker update latest_unicorns
you must provide one or more flags when using this command
root@dice-devops:/home/Repos/devopslive1.1# dcoker ps
Command 'dcoker' not found, did you mean:
  command 'docker' from snap docker (20.10.24)
  command 'docker' from deb docker.io (24.0.5-0ubuntu1~22.04.1)
  command 'docker' from deb podman-docker (3.4.4+ds1-1ubuntu1.22.04.2)
See 'snap info <snapname>' for additional versions.
root@dice-devops:/home/Repos/devopslive1.1# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED        STATUS          PORTS                                       NAMES
1c421046eb02   unicorn:v1   "python3 main.py"        4 hours ago    Up 27 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   latest_unicorns
8b121467c308   nginx        "/docker-entrypoint.…"   17 hours ago   Up 17 hours                                                 pedantic_nash
3ea6aa7e4382   nginx        "/docker-entrypoint.…"   42 hours ago   Up 42 hours     80/tcp                                      blissful_shtern
root@dice-devops:/home/Repos/devopslive1.1#

root@dice-devops:/home/Repos/devopslive1.1# docker attach latest_unicorns
.INFO:     103.85.36.175:59380 - "GET / HTTP/1.1" 200 OK



root@dice-devops:/home/Repos/devopslive1.1# docker port latest_unicorns
8000/tcp -> 0.0.0.0:8000
8000/tcp -> [::]:8000



```



