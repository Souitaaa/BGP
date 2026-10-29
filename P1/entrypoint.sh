#!/bin/sh

ospfd -d && isisd -d && bgpd -d && zebra -d

exec /usr/sbin/watchquagga ospfd bgpd isisd zebra
