from http.server import BaseHTTPRequestHandler, HTTPServer
import json
host_name = "localhost"
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки входящих запросов"""

    def do_GET(self):
        """Метод для обработки GET-запросов"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("contacts.html", encoding='utf-8') as file:
            data = file.read()
            print(data)

        self.wfile.write(bytes(data, 'utf-8'))

    def do_POST(self):
        """Метод для обработки POST-запросов"""

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_length)

        data = json.loads(post_data.decode('utf-8'))

        print('Имя:', data.get('name'))
        print('Почта:', data.get('email'))
        print('Сообщение:', data.get('message'))

        response = {'status': 'success', 'message': 'Данные получены'}
        self.wfile.write(json.dumps(response).encode('utf-8'))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)

    try:

        web_server.serve_forever()
    except KeyboardInterrupt:

        pass


    web_server.server_close()
    print("Server stopped.")

    from http.server import BaseHTTPRequestHandler, HTTPServer





def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

