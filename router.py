import telnetlib
import getpass

user = input("Enter the Telnet Username: ")
password = getpass.getpass("Enter the telnet password: ")

HOST = '192.168.20.129'
print("Telnet to host: " + HOST)
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"configure terminal\n")
    tn.write(b"int loopback 0\n")
    tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
    tn.write(b"exit\n")

    tn.write(b"int g0/1\n")
    tn.write(b"ip address 172.16.1.1 255.255.255.0\n")
    tn.write(b"exit\n")
    
    tn.write(b"ip dhcp exclude 172.16.1.1 172.16.1.100\n")
    tn.write(b"ip dhcp pool R1\n")
    tn.write(b"network 172.16.1.0 255.255.255.0\n")
    tn.write(b"default 172.16.1.1\n")
    tn.write(b"dns 8.8.8.8\n")
    tn.write(b"exit\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"show ip int br\n")
tn.write(b"exit\n")
print(tn.read_all().decode())