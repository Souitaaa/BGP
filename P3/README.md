# Part 3 — BGP with EVPN

Linux commands and routing-console commands are stored separately because they run in different interpreters.

| Equipment | Linux shell | vtysh console |
| --- | --- | --- |
| R2 | `linux/r2_setup.sh` | Missing |
| R3 | `linux/r3_setup.sh` | `vtysh/r3.conf` |
| R4 | `linux/r4_setup.sh` | `vtysh/r4.conf` |
| R1 / route reflector | Missing | Missing |

The Linux scripts were split from the original `p3/setup1.sh`, which contained repeated setup blocks for R2, R3, and R4. Run only the matching script on each node with `sh`.

The `.conf` files were previously named `.sh` but contain vtysh commands. Enter their contents in the corresponding router's `vtysh` console, not a Linux shell. They preserve the existing OSPF, loopback, BGP AS 1, and EVPN commands, including the peer at `1.1.1.1`.

## Configuration to review and complete

- Add R1's route-reflector configuration, R2's routing configuration, and host configurations.
- Verify interface mapping against the actual topology: the Linux scripts bridge `eth1`, while R3's routing configuration assigns an OSPF underlay address to `eth1`.
- Verify R3's hostname (`csouita-2`) and loopback (`1.1.1.2`) against its intended equipment identity; standardize equipment names with your login.
- Complete and verify the VTEP/underlay configuration and confirm that the routing image supports the EVPN commands used here.
- Export the completed topology with base images as `P3.gns3project`.

The existing configuration has been reorganized, not validated in a running GNS3 topology.
