from socket import *
from uuid import getnode as get_mac
import re, uuid
import time
from ArpCacheItem import ArpCacheItem
import pprint

"""
This class encapsulates the Arp cache and the corresponding function to add values to the cache
"""


class ArpCache:
    NetworkCache = {
        "192.168.1.1": "00:0A:95:9D:68:16",
        "192.168.1.2": "00:0A:95:9D:68:17",
        "192.168.1.3": "00:0A:95:9D:68:18",
        "192.168.1.4": "00:0A:95:9D:68:19",
        "192.168.1.5": "00:0A:95:9D:68:1A",
    } #dummy data
    MyHostName = gethostname()
    MyIP = gethostbyname(MyHostName)
    MyMac = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    MaxCacheSize = 6
    
    """
    If max cache size is reached first entry is removed and then the new entry is added
    """

    def AddMac(ip, mac):
        """
        This function checks if the cache is full and deletes the first enrty before
        adding new ones.

        Args:
            param1:Ip address queried
            param2:Corresponding MAC address
        """
       
        if len(ArpCache.NetworkCache) >= ArpCache.MaxCacheSize:
            (k := next(iter(ArpCache.NetworkCache)), ArpCache.NetworkCache.pop(k))
        ArpCache.NetworkCache[ip] = mac

    def GetMac(ip):
        """
        This function gets retrieves MAC address of the device

        Args:
            param1:IP address queried
        """
        mac = ArpCache.NetworkCache.get(ip, "x")
        return mac

    def PrintArps():
        """
        This function prints the ARP cache
        """
        print(
            "Current ARP Table:\nIP Address\tMAC Address\n"
            + "\n".join(f"{k}: {v}" for k, v in ArpCache.NetworkCache.items()),
        )
