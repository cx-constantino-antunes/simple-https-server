from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

CERT_FILE="cert/cert.pem"
KEY_FILE="cert/key.pem"

# Define a custom handler class
class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        msg = b"It works!\n"
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", len(msg))
        self.end_headers()
        # Write the response content
        self.wfile.write(msg)  # Use bytes to send the response

# Define server address and port
server_address = ('localhost', 4443)

# Create the HTTP server instance
httpd = HTTPServer(server_address, CustomHandler)

# Create SSL context and wrap the server socket
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)  # Load certificate and key

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on {server_address[0]} port {server_address[1]}...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    httpd.server_close()
