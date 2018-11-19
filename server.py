"""
Python Webserver
 - 11/19/2018
 - Austin Rovge

This is a simple web server written in python.
"""

import socket


def main():
    """
    The main method is called first and starts the server on port 8080.
    """

    start_http_server(8080)


def start_http_server(port):
    """
    This method setups the http server.
    :param port: the port to start the server on
    """

    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to the local address on the specified port
    listen_addr = '', port
    server_socket.bind(listen_addr)

    # listen for an 10 requests. refuse any after that
    server_socket.listen(10)

    while True:
        conn, addr = server_socket.accept()
        handle_request(conn)


def handle_request(server_socket):
    request_line, request_headers = read_http_request(server_socket)
    http_request, resource, protocol_version = request_line.split(' ', 3)

    if http_request == 'GET':
        print('GET HTTP request')
    else:
        print(f'{http_request} requests are not supported')


def read_http_request(server_socket):
    """
    This method reads in the entire HTTP request.
    :param server_socket: the socket to read bytes from
    :return: a tuple of the request line and the request headers, in ASCII
    """

    # all HTTP requests ends with a \r\n\r\n (CR LF CR LF)
    http_request = b''
    while b'\r\n\r\n' not in http_request:
        http_request += next_byte(server_socket)

    request_line, request_headers = http_request.decode('ASCII').split('\r\n', 1)

    return request_line, request_headers


def next_byte(server_socket):
    """
    This method reads in one byte.
    :param server_socket: the socket to read one byte from
    :return: a byte object of the single byte read in
    """

    return server_socket.recv(1)


if __name__ == '__main__':
    main()
