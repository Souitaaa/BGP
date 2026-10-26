#R2

ip link add vxlan10 type vxlan id 10 dstport 4789 # create the vxlan interface
ip link set vxlan10 up # enable the vxlan

ip link add name br0 type bridge # create the bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0

#R3

ip link add vxlan10 type vxlan id 10 dstport 4789 # create the vxlan interface
ip link set vxlan10 up # enable the vxlan

ip link add name br0 type bridge # create the bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0

#R4

ip link add vxlan10 type vxlan id 10 dstport 4789 # create the vxlan interface
ip link set vxlan10 up # enable the vxlan

ip link add name br0 type bridge # create the bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0
