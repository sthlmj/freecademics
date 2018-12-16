from http.server import BaseHTTPRequestHandler

from header import header
from os import curdir, sep

class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
    return
    
  def do_GET(self):
    if self.path=="/":
        self.path="/index.html"
    sendReply = False
    if self.path.endswith(".html"):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
		
        self.end_headers()
        # Start
        self.wfile.write(bytes("<html>" +
        "<head>" +
        "<link rel=\"stylesheet\" type=\"text/css\" href=\"head.css\">" + 		
        "</head>" + 
		"<body bgcolor=\"#487cbc\">", "UTF-8"))
        # Document header
        self.wfile.write(header())
        # Document body
        content = bytes("Hello World2", "UTF-8")
        self.wfile.write(content)
        # End		
        self.wfile.write(bytes("</body>" + 
        "</html>", "UTF-8"))
        

        sendReply = False
    if self.path.endswith(".jpg"):
        mimetype='image/jpg'
        sendReply = True
    if self.path.endswith(".gif"):
        mimetype='image/gif'
        sendReply = True
    if self.path.endswith(".png"):
        mimetype='image/png'
        sendReply = True
    if self.path.endswith(".js"):
        mimetype='application/javascript'
        sendReply = True
    if self.path.endswith(".css"):
        mimetype='text/css'
        sendReply = True

    if sendReply == True:
        #Open the static file requested and send it
        f = open(curdir + sep + self.path, 'rb') 
        self.send_response(200)
        self.send_header('Content-type',mimetype)
        self.end_headers()
        self.wfile.write(f.read())
        f.close()
  
  def do_POST(self):
    return
