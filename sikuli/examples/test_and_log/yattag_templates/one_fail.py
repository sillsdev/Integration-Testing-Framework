from __future__ import with_statement
from yattag import Doc

def template(clicked_image, expected_screen, screencap):
	doc, tag, text = Doc().tagtext()
	doc.asis('<!DOCTYPE html>')

	with tag("html", lang="en_us"):
		with tag("head"):
			with tag("title"):
				text("Test page")
		with tag("body"):
			with tag("table"):
                                with tag("tr"):
                                        with tag("th"):
                                                text("Clicked")
                                        with tag("th"):
                                                text("Expected")
                                        with tag("th"):
                                                text("Screenshot")
				with tag("tr"):
					with tag("td"):
						doc.stag("img", src=clicked_image)
					with tag("td"):
						if expected_screen is not None:
							doc.stag("img", src=expected_screen)
					with tag("td"):
						if screencap is not None:
							doc.stag("img", src=screencap, height="25%", width="25%")

	return doc
