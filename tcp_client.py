import socket
import sys

host = 'gaia.cs.umass.edu'
port = 80  # web

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('# Sending data to server')
request = (b'GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n')

try:
    s.sendall(request)
except socket.error:
    print ('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(8192)

print (reply)

# Write response
print('# Writing the data from server in a file')
f= open("response.html","w+")
f.write(reply.decode("utf-8"))
f.close()
print('# Finished!')