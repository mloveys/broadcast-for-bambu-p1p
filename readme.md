# Broadcast for Bambu P1P Printer

The python script included was made so I could use Bambu Studio without the need for an internet connection. Additionally, I wanted the printer to be isolated on an IoT vlan with a statically assigned ip address, allowing only necessary traffic.

For discovery, the printer uses SSDP protocol, and this python script will replicate what the printer sends.

You will need to replace the following values in the script:

- `10.10.10.10` with the ip address of the printer
- `000000000000000` with the serial number of the printer

Once updated, run the script and it will broadcast the packet on the local interface
