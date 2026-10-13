# Servidor local para probar los datos enlazados en http://localhost:8000/
# Uso: colócalo en la misma carpeta que los .ttl y ejecuta:  python servidor.py
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class TurtleHandler(SimpleHTTPRequestHandler):
    # Sirve los .ttl con su tipo MIME correcto (y en UTF-8 para las tildes)
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,
                      ".ttl": "text/turtle; charset=utf-8"}

    def end_headers(self):
        # Permite que el Turtle Web Editor u otras herramientas lean los archivos
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == "__main__":
    print("Sirviendo en http://localhost:8000/indice.ttl  (Ctrl+C para detener)")
    ThreadingHTTPServer(("localhost", 8000), TurtleHandler).serve_forever()
