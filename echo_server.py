import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('localhost', 10000)
    # TCP socket with IPv4 Addressing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    # address error if socket already open
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # bind socket and listen for incoming connections
    sock.bind(address)
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # new socket when a client connects called 'conn',

            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers

                while True:
                    # 5eceive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.

                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))

                    # Send the data you received back to the client

                    #if len(data) < 16:
                    if not data:
                        break

            finally:
                # Cleaning up the open connection
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        print('quitting echo server', file=log_buffer)
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)
