from socket import *
from ArpCache import ArpCache
from uuid import getnode as get_mac
import re, uuid


SERVER_PORT = 65432


class ArpServer:
    def StartServer(self):
        """
        This is the client side function
        """
        try:
            with socket(AF_INET, SOCK_DGRAM) as s:
                s.bind(("", SERVER_PORT))
                print(
                    "ARP server is listening..."
                    + "\nMyIP: "
                    + ArpCache.MyIP
                    + "\nMyMac: "
                    + ArpCache.MyMac
                )
                # Keep the server running
                while True:
                        with s:
                            while True:
                                """
                                IP is received from the client. If it matches with the device IP then the 
                                MAC address of the device is sent to the client
                                """
                                receivedIp, addr = s.recvfrom(1024)
                                receivedIp = receivedIp.decode("utf-8")
                                if receivedIp == ArpCache.MyIP:
                                    mac = ArpCache.MyMac
                                else:
                                    mac = "x"

                                mac = mac.encode("utf-8")
                                s.sendto(mac, addr)
                                print(
                                    f"Received ARP request for IP: {receivedIp}. Responded with: {mac}"
                                )
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            input("Press Enter to exit...")
