import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		node = HTMLNode("This is a text node", "Middle text", props="Give props")
		node2 = HTMLNode("This is a text node", "Middle text", None ,"Give props")
		self.assertEqual(node, node2)

	def test_repr(self):
		text_in = ("This is more text, blah, blah")
		node = HTMLNode(text_in, text_in, text_in, text_in)
		node2 = f"HTMLNode({text_in}, {text_in}, {text_in}, {text_in})"
		self.assertEqual(repr(node), node2)

	def test_not_eq(self):
		node = HTMLNode("This is a text node", None, "...more test node...", None)
		node2 = HTMLNode("This is a text node", None, None, None)
		self.assertNotEqual(node, node2)

#	def test_exception(self):
#		with self.assertRaises(AssertionError):
#			HTMLNode("This is an test of the emergency Exception system.")

if __name__ == "__main__":
	unittest.main()
