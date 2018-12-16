def header():
	return bytes("" +
	"<img src=\"logo.png\"></img>" + 
	"<br />"
	"<div class=\"topnav\">" + 
	"<a class=\"active\" href=\"home\">Hem</a>" + 
	"<a href=\"about\">Annonsera</a>" + 
	"<a href=\"contact\">Contact</a>" + 
	"<input type=\"text\" placeholder=\"Sök..\">" + 
	"</div>" 
	, "UTF-8")