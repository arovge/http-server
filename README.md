# http-server
This project is for utilizing low level network protocols to create a functioning HTTP server in Python. Individual bytes are sent and read across the network.

This project does not utilize any libraries for reading the data, besides ones for creating TCP sockets and such.

### HTTP Messages
An HTTP request is made of the request line and the headers.

Here is the status line.
```status line
GET / HTTP/1.1
```

And the headers:
```http headers
Host: localhost:8080
Connection: keep-alive
Cache-Control: max-age=0
...
```

An HTTP response is the same as this but it will have a body and a header specified how that body should be read by the client.

The status line and each header is separated by a CR LF (\r\n). The headers end with an additional CR LF before the body starts in a response.

This simple HTTP server will handle reading in each individual byte until it reaches a specific number of bytes or the ending CR LF specified in the HTTP protocol.

### HTTP Requests
GET and POST requests are the only two supported HTTP protocols at this time. A 405 HTTP response is sent whenever an unsupported HTTP request is received.

This server handles invalid file requests by sending a 404 HTTP response. A HTML file is not sent with this.

### Future Development
* add proper handling for POST requests
* add chunking support for returning objects
