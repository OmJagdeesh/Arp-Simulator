from socket import *
from ArpCache import ArpCache
import time



BROADCAST_IP = "YOUR_BROADCAST_IP"  # Replace with your broadcast IP address
SERVER_PORT = 65432
"""
Broadcast IP will change depending on the network you are connected to
"""


class ArpClient:

    def StartClient(self):
        """
        This is the client side function
        """
        ArpCache.PrintArps()
        try:
            while True:
                ip = input("Enter IP to ARP for or 'x' to exit: ")
                if ip == "x":
                    break
                mac = ArpCache.GetMac(ip)
                """
                If IP is already present in arp cache prints the same, else broadcasts the IP to server
                and receives the corresponding MAC adrress.
                """
                if mac != "x":
                    print("Ip already present in Arp cache " + mac)
                    # break
                with socket(AF_INET, SOCK_DGRAM) as s:
                    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
                    s.sendto(ip.encode("utf-8"), (BROADCAST_IP, SERVER_PORT))
                    time.sleep(1 / 5)
                    mac, addr = s.recvfrom(1024)
                    mac = mac.decode("utf-8")
                """
                The new IP address and the corresponding MAC address is added to the ARP cache
                """
                if mac != "x":
                    ArpCache.AddMac(ip, mac)
                    print(f"Received ARP reply: {ip} is at {mac}")
                else:
                    print(f"No ARP Reply for {ip}")

                ArpCache.PrintArps()
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
