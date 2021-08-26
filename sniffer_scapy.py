from scapy.all import *

def main():
	sniff(prn=http_header, filter="tcp port 80")

def http_header(packet):
	http_packet=str(packet)
	if http_packet.find('GET'):
		return print_packet(packet)

def print_packet(packet1):
	ret = "-------------------------------[ Received Packet ] -------------------------------\n"
	ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
	ret += "---------------------------------------------------------------------------------\n"
	return ret

if __name__ == '__main__':
	main()
