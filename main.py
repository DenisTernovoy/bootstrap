from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080

class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки входящих запросов"""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("contacts.html", encoding='utf-8') as file:
            data = file.read()
            # print(data)

        self.wfile.write(bytes(data, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        web_server.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

        # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    web_server.server_close()
    print("Server stopped.")