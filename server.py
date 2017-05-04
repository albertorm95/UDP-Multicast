import socket
import struct
import sys

multicast_group = "224.3.29.71"
server_address = ("", 1111)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
# Receive/respond loop
while True:
    print "\nEsperando a recibir mensajes"
    data, address = sock.recvfrom(1024)
    
    print "Recibi %s bytes de %s" % (len(data), address)
    print data

    print "Enviando acknowledgement a" + str(address)
    sock.sendto("acknowledgement", address)