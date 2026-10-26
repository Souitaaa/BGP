# Create the Multicast VXLAN tunnel
ip link add vxlan10 type vxlan id 10 dstport 4789 group 239.1.1.1 dev eth0 ttl auto
ip link set up dev vxlan10
ip addr add 32.1.1.253/24 dev vxlan10

# Create the internal bridge
ip link add name br0 type bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0