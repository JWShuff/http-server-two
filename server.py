import socket
import datetime
from request import Request
from jinja2 import Template


def build_html_response(text_body):

    html_body = f"<html><head><title>An Example Page</title></head><body>{text_body}</body></html>"
    return f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(html_body)}\n\n{html_body}"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# so you don't have to change ports when restarting
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 9292))

while True:
    server.listen()
    client_connection, _client_address = server.accept()
    client_request = Request(client_connection)
    if client_request.parsed_request['uri'] == '/':
        client_connection.send(build_html_response('Hello World').encode())
    elif client_request.parsed_request['uri'] == '/time':
        with open('./templates/time.html', 'r') as myFile:
            html_from_file = myFile.read()
        template = Template(html_from_file)
        body_response = template.render(time=datetime.datetime.now())
        body_response = (build_html_response(body_response))
        client_connection.send(body_response.encode())
    client_connection.close()
