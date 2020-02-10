import socket

HOST = 'gaia.cs.umass.edu'  # The server's hostname or IP address
PORT = 80        # The port used by the server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print ("Socket successfully created")
        s.connect((HOST, PORT))
        s.send(b'GET /kurose_ross/interactive/index.php HTTP/1.1 Host: gaia.cs.umass.edu \r\n')
        data = s.recv(1024)
        while (len(data) > 0):
            print(data)
            data = s.recv(10000)

except socket.error as err: 
    print ("socket creation failed with error %s") %(err)  

#print('Received', repr(data))