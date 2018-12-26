def header():
	return bytes("" +
	"<img src=\"logo.png\"></img>" + 
	"<br />"
	"<div class=\"topnav\">" + 
	"<a class=\"active\" href=\"index\">Hem</a>" + 
	"<a href=\"assignments\">Uppdrag</a>" + 
	"<a href=\"freelancers\">Frilansare</a>" + 
	"<input type=\"text\" placeholder=\"S&ouml;k..\">" + 
	"</div>" 
	, "UTF-8")