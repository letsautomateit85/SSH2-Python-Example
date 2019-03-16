#Let's Automate It - SSH2-Python - Remotely connecting to a Cisco Device

import socket
from ssh2.session import Session

host = '192.168.1.150'
user = 'cisco'
password = 'cisco'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,22))

session = Session()
session.handshake(sock)
session.userauth_password(user, password)

channel = session.open_session()
channel.execute('show run')
size, data = channel.read()
while size > 0:
    print(data.decode())
    size, data = channel.read()
channel.close()
print("Exit status: {0}".format(channel.get_exit_status()))
