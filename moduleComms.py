import socket
ipAddress = "192.168.1.26"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipAddress, 2222))

