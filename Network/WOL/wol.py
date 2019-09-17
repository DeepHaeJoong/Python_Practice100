'''
매직패킷은 16진수 FF 상수값이 6번 반복 + 대상 컴퓨터의 mac address가 16번 반복(16진수)
'''

import struct
import socket
import os


mycoms = {
    "pc1" : "AA-BB-CC-DD-EE-FF",
    "pc2" : "11-22-33-44-55-66",
    "Xeon" : "2C-FD-A1-34-32-10",
    "GPU Server" : "48-A4-72-77-54-C5"
}

def wake_on_lan(mac):
    # 켜질 컴퓨터의 Mac 주소
    addrs = mac.split("-")
    hw_addr = struct.pack("BBBBBB",
                          int(addrs[0], 16),
                          int(addrs[1], 16),
                          int(addrs[2], 16),
                          int(addrs[3], 16),
                          int(addrs[4], 16),
                          int(addrs[5], 16))

    magic = b"\xFF" * 6 + hw_addr * 16
    # print(magic)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(magic, ('192.168.0.255', 7))
    s.close()


if __name__ == "__main__":
    os.system("cls")
    count = 1
    for name, mac in mycoms.items():
        print("{} {} {}".format(count, mac, name))
        count += 1
    print("*"*60)
    select = int(input("매직패킷을 보낼 PC 번호를 입력하세요"))
    name, mac = list(mycoms.items())[select-1]
    print(name, mac)
    wake_on_lan(mac)
