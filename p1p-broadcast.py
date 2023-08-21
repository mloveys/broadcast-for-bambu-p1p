#!/usr/bin/env python3

import sys
import socket

SSDP_ADDR = "255.255.255.255";
SSDP_PORT = 2021;

ssdp_content = "NOTIFY * HTTP/1.1\r\n" + \
               "HOST: 239.255.255.250:1900\r\n" + \
               "Server: Buildroot/2018.02-rc3 UPnP/1.0 ssdpd/1.8\r\n" + \
               "Location: 10.10.10.10\r\n" + \
               "NT: urn:bambulab-com:device:3dprinter:1\r\n" + \
               "USN: 000000000000000\r\n" + \
               "Cache-Control: max-age=1800\r\n" + \
               "DevModel.bambu.com: C11\r\n" + \
               "DevName.bambu.com: 3DP-01S-174\r\n" + \
               "DevSignal.bambu.com: -30\r\n" + \
               "DevConnect.bambu.com: lan\r\n" + \
               "DevBind.bambu.com: free\r\n" + \
               "Devseclink.bambu.com: secure\r\n" + \
               "\r\n"

ssdp_content = bytes(ssdp_content, 'utf-8')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to localhost so we send to loopback
sock.bind(('127.0.0.1', 1900))

# Set Packet Type to Broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Finally send out the interface
sock.sendto(ssdp_content, (SSDP_ADDR, SSDP_PORT))
