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

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    listen_addr = '', port
    server_socket.bind(listen_addr)
    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        handle_request(conn)


def handle_request(server_socket):
    print(read_http_request(server_socket))


def read_http_request(server_socket):
    """
    This method reads in the entire HTTP request line.
    :param server_socket: the socket to read bytes from
    :return: the http request as a bytes object
    """

    http_request = b''

    # all HTTP requests ends with a \r\n\r\n (CR LF CR LF)
    while b'\r\n\r\n' not in http_request:
        http_request += next_byte(server_socket)

    return http_request


def next_byte(server_socket):
    """
    This method reads in one byte.
    :param server_socket: the socket to read one byte from
    :return: a byte object of the byte read in
    """

    return server_socket.recv(1)


if __name__ == '__main__':
    main()
