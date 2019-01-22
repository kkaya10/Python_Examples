import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("[+] Enter Target IP: ")
port_list = list()

def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

while True:
    target_ports = int(input("[+] Type port numbers which you want to scan , type 0 to exit !"))

    if target_ports != 0:
        port_list.append(target_ports)
    elif target_ports == 0:
        break

for portNumber in range(1,len(port_list)):
    print("Scanning port", port_list[portNumber])
    if scanner(port_list[portNumber]):
        print('[*] Port', port_list[portNumber], '/tcp','is open')
    else:
        print('[*] Port', port_list[portNumber], '/tcp','is closed')
