import socket
from datetime import datetime
target = input("Enter the IP address or hostname to scan: ")
start_port = 1
end_port = 1025
print(f"\nStarting scan on {target}...\n")
start_time = datetime.now()
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            s.sendall(b"hello\r\n")
            banner = s.recv(1024).decode().strip()
            print(f"Port {port} is OPEN - Banner: {banner}")
        except:
            print(f"Port {port} is OPEN - no banner returned")