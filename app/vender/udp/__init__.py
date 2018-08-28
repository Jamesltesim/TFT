from socket import *
from time import ctime


# host '127.0.0.1'
# port 12345
# msg 'message'
def sendto(host,port,msg):
    udpServer = socket(AF_INET,SOCK_DGRAM)
    udpServer.sendto(msg.encode(encoding='utf-8'),(host,port))
    print('at %s send to %s : %s',ctime(),(host,port),msg)
    udpServer.close()