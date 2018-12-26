from http.server import BaseHTTPRequestHandler


from os import curdir, sep
from header import header
from index import index
from assignments import assignments
from freelancers import freelancers

class Server(BaseHTTPRequestHandler):
	def do_HEAD(self):
		return
	
	def do_GET(self):
		if self.path=="/":
			self.path="/index"
		sendReply = False
		if self.path.endswith("index") or self.path.endswith("assignments") or self.path.endswith("freelancers"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			
			self.end_headers()
			# Start
			self.wfile.write(bytes("<html>" +
			"<head>" +
			"<link rel=\"stylesheet\" type=\"text/css\" href=\"head.css\">" + 		
			"<!-- Latest compiled and minified CSS -->" +
			"<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\" integrity=\"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u\" crossorigin=\"anonymous\">" +
			"<!-- Optional theme -->" +
			"<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css\" integrity=\"sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp\" crossorigin=\"anonymous\">" +
			"<!-- Latest compiled and minified JavaScript -->" + 
			"<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\" integrity=\"sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa\" crossorigin=\"anonymous\"></script>" + 
			"</head>" + 
			"<body bgcolor=\"#487cbc\">", "UTF-8"))
			# Document header
			self.wfile.write(header())
			# Document body
			if self.path.endswith("index"):
				self.wfile.write(index())
			elif self.path.endswith("assignments"):
				self.wfile.write(assignments())
			elif self.path.endswith("freelancers"):
				self.wfile.write(freelancers())
			# End		
			self.wfile.write(bytes("</div></body>" + 
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
