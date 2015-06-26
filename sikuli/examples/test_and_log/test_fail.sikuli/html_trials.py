import xml.etree.ElementTree as ETree

from jinja2 import Environment, FileSystemLoader
from mako.lookup import TemplateLookup
from yattag import indent
from yattag_templates.thing_yattag import template


class TestData:
	def __init__(self, thing1, thing2=None, thing3=None):
		self.thing1 = thing1
		if thing2 is not None:
			self.thing2 = thing2
			if thing3 is not None:
				self.thing3 = thing3
				self.type = 2
			else:
				self.type = 1
		else:
			self.type = 0

def add_failed_test(root, text):

	paragraph = ETree.SubElement(root, "p")
	paragraph.text = text


def element_tree():

	# Create the html document tree and set its title.
	root = ETree.Element("html")
	head = ETree.SubElement(root, "head")
	title = ETree.SubElement(head, "title")
	title.text = "Hello World!"

	body = ETree.SubElement(root, "body")
	for i in range(5):
		add_failed_test(body, str(i))

	# Write tree to file.
	tree = ETree.ElementTree(root)
	tree.write("my_tree.html", method="xml")

def jinja():
	env = Environment(loader=FileSystemLoader(""))
	template = env.get_template("thing_jinja2.html")
	stuff = [TestData("a"), TestData("b", 0), TestData("c", 2, 56.2), TestData("a", 3)]

	t = template.render(failed_test_data=stuff)
	print t
	with open("thing_filledin.html", "w") as f:
		f.write(t)

def mako(log_file_name="thing_filledin_mako.html"):

	mylookup = TemplateLookup(directories=['.', "./mako_templates"])

	templ = mylookup.get_template("thing_mako.html")
	stuff = [TestData("a"), TestData("b", 0), TestData("c", 2, 56.2), TestData("a", 3)]
	t = templ.render(failed_test_data=stuff)
	with open(log_file_name, "w") as f:
		f.write(t)

def yattag(log_file_name="thing_filledin_yattag.html"):
	stuff = [TestData("a"), TestData("b", 0), TestData("c", 2, 56.2), TestData("a", 3)]
	t = indent(template(stuff).getvalue())
	with open(log_file_name, "w") as f:
		f.write(t)