import socket
import argparse

parser = argparse.ArgumentParser(description='Obtener servidor banner')

# Main arguments
parser.add_argument("-target", dest="target", help="target IP", required=True)
parser.add_argument("-port", dest="port", help="Port", type=int, required=True)
parsed_args = parser.parse_args()
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((parsed_args.target, parsed_args.port))	
sock.settimeout(2)
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % parsed_args.target
data = ''
try:
    sock.sendall(request.encode())
    data = sock.recv(1024).decode("utf-8")
    print(data)
except socket.error:
	print ("Socket error", socket.errno)
finally:
	print("closing connection")
	sock.close()
