from __future__ import with_statement
from sikuli import *
from yattag import Doc
import type0, type1, type2

def template(failed_test_data):
	doc, tag, text = Doc().tagtext()
	doc.asis('<!DOCTYPE html>')

	with tag("html", lang="en_us"):
		with tag("head"):
			with tag("title"):
				text("Test page")
		with tag("body"):
			with tag("ul"):
				for fail in failed_test_data:
					if fail.type == 0:
						doc.asis(type0.template(fail))
					elif fail.type == 1:
						doc.asis(type1.template(fail))
					else:
						doc.asis(type2.template(fail))

	return doc
