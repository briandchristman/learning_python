import sys
import socket
destIP = sys.argv
destPort = sys.argv

def port_test(destIP,destPort):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(2)                                      #2 Second Timeout
  result = sock.connect_ex((sourceIP,portNum))
  if result == 0:
    print ('port OPEN')
  else:
    print ('port CLOSED, connect_ex returned: '+str(result))

# if __name__ == '__main__':
  # port_test(desetIP,destPort)
