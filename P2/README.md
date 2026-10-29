# Part 2 — Discovering VXLAN

The existing commands implement the multicast variant using VNI `10`, bridge `br0`, and multicast group `239.1.1.1`.

| Equipment | Linux shell script |
| --- | --- |
| Host 1 | `hosts/h1_setup.sh` |
| Host 2 | `hosts/h2_setup.sh` |
| Router 1 | `multicast/r1_setup.sh` |
| Router 2 | `multicast/r2_setup.sh` |

Copy each script to its corresponding GNS3 node and run it with `sh`. Router scripts use `eth0` for the VXLAN underlay and bridge `eth1` to the tunnel. Configure working underlay connectivity before running them. Host scripts assign addresses on `eth1` and default gateways.

The original commands are preserved, including the gateway addresses assigned to the VXLAN interfaces. Verify interface/address placement and connectivity in the lab.

Still required: static unicast VXLAN configuration (the subject requires static mode first), underlay configuration, equipment names containing your login, and a portable project export including base images (`P2.gns3project`).
