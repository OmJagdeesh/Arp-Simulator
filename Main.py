from ArpClient import ArpClient
from ArpServer import ArpServer
import socket

"""
Takes choice input from user and initiates the corresponding fucntion
"""
choice = input("Enter 1 to start server or 2 to start client : ")
if choice == "1":
    s1 = ArpServer()
    s1.StartServer()
elif choice == "2":
    c1 = ArpClient()
    c1.StartClient()
else:
    print("Invalid choice")
