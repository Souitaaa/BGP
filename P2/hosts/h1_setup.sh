#!/bin/sh

# Assign IP and default gateway
ip addr add 32.1.1.1/24 dev eth1
route add default gw 32.1.1.254
