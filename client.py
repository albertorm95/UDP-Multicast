import socket
import struct

message = "MENSAJE"
multicast_group = ("224.3.29.71", 1111)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(5)
# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack("b", 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send data to the multicast group
print "Enviando: " + message
sock.sendto(message, multicast_group)

# Look for responses from all recipients
while True:
    print "Esperando respuesta..."
    data, server = sock.recvfrom(16)
    if not data:
        break
    elif data == "bye":
        sock.close()
        break
    else:
        print "Recibi %s de %s" % (data, server)
