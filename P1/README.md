# Part 1 — GNS3 with Docker

- `Dockerfile.vim`: Alpine host image with BusyBox (provided by Alpine) and Vim.
- `Dockerfile.routing`: Alpine routing image with Quagga and Tini.
- `entrypoint.sh`: starts OSPF, IS-IS, BGP, and Zebra, then monitors the daemons.

Build from the repository root so the routing Dockerfile can copy its entrypoint:

```sh
docker build -t badass-host -f P1/Dockerfile.vim P1
docker build -t badass-routing -f P1/Dockerfile.routing P1
```

Import both images into GNS3, use equipment names containing your login, and leave IP addresses unconfigured for this part. The routing image creates empty daemon configuration files; configure and verify the services in the lab.

Still required: the GNS3 topology, commented per-equipment configuration, and a portable project export including base images (`P1.gns3project`).
