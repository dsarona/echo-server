import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # a TCP socket with IPv4 Addressing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)

    # connect your socket to the server
    sock.connect(server_address)
    received_message = ''
    #msg = input("> ")

    try:

        print('sending "{0}"'.format(msg), file=log_buffer)
        # send your message to the server
        sock.sendall(msg.encode('utf-8'))

        # Server should be sending you back your message as a series
        #       of 16-byte chunks
        # chunk = b''
        bytes_sent = len(msg)
        bytes_recv = 0

        while bytes_recv < bytes_sent:
            chunk = sock.recv(16)
            bytes_recv += len(chunk)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

            received_message += chunk.decode('utf8')
            print('received "{0}"'.format(chunk), file=log_buffer)
    finally:
        # close your client socket.
        sock.close()
        print('closing socket', file=log_buffer)

        # When all is said and done, you should return the entire reply
        return received_message

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
