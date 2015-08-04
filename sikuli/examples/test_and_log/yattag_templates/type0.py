from __future__ import with_statement
from yattag import Doc

def template(fail):
	doc, tag, text = Doc().tagtext()
	with tag("li"):
		text("just " + str(fail.thing1))
	return doc.getvalue()
