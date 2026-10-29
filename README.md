# BADASS — BGP and VXLAN

Project files are grouped into the root folders required by the subject:

- `P1/`: Docker images and routing-container startup.
- `P2/`: host setup and multicast VXLAN router commands.
- `P3/`: Linux VXLAN/bridge setup and routing commands for BGP EVPN.

The reference subject is `en.subject (1).pdf`. Each part has its own README with execution instructions and remaining requirements. Existing network commands and addresses have been preserved.

Run network setup inside the corresponding GNS3 node, with root privileges. These commands change network interfaces and routes and are intended for a fresh lab node; they are not idempotent.

## Submission status

This reorganization does not constitute a complete implementation of the subject. Static VXLAN configuration for P2, some P3 equipment configurations, and the portable GNS3 project exports are still missing. Export each completed topology from GNS3 using **File → Export portable project**, including its base images, and place the resulting ZIP-format `.gns3project` file in the corresponding `P1`, `P2`, or `P3` folder.

## Start all machines

With Python 3 installed and the GNS3 server running, open your imported topology in GNS3 and run:

```sh
./start_all.py
```

This powers on every node in every currently open GNS3 project. It prints the resulting node counts and exits with an error if a node did not start. It does not create topologies or apply the network setup scripts.

To list projects or start one specific project (including a closed project):

```sh
./start_all.py --list
./start_all.py --project P2
./start_all.py --server http://192.168.56.101:3080 --project P3
```

Names must match exactly; a project UUID also works. The default controller is `http://localhost:3080` using the GNS3 v2 API. Set `GNS3_SERVER` to change the default server, or pass `--api-version v3` for a v3 server. For authentication, set `GNS3_USER` and `GNS3_PASSWORD` for Basic authentication, or `GNS3_TOKEN` for a Bearer token. Credentials are read from the environment.

API reference: [GNS3 start-all-nodes endpoint](https://api.gns3.net/en/latest/api/v2/controller/node/projectsprojectidnodesstart.html).
