import platform
import socket
import datetime

with open("system_log.txt", "w") as log:
    log.write(f"System Log - {datetime.datetime.now()}\n")
    log.write(f"="*40 + "\n")
    log.write(f"OS: {platform.system()} {platform.release()}\n")
    log.write(f"Machine: {platform.machine()}\n")
    log.write(f"Processor: {platform.processor()}\n")
    log.write(f"Hostname: {socket.gethostname()}\n")
    log.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
