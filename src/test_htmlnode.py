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
		node2 = f"HTMLNode({text_in}, {text_in}, children: {text_in}, {text_in})"
		self.assertEqual(repr(node), node2)

	def test_not_eq(self):
		node = HTMLNode("This is a text node", None, "...more test node...", None)
		node2 = HTMLNode("This is a text node", None, None, None)
		self.assertNotEqual(node, node2)

	def test_to_html_props(self):
		node = HTMLNode(
			"div",
			"Hello, world!",
			None,
			{"class": "greeting", "href": "https://boot.dev"},
		)
		self.assertEqual(
			node.props_to_html(),
			' class="greeting" href="https://boot.dev"',
		)

	def test_values(self):
		node = HTMLNode(
			"div",
			"I wish I could read",
		)
		self.assertEqual(
			node.tag,
			"div",
		)
		self.assertEqual(
			node.value,
			"I wish I could read",
		)
		self.assertEqual(
			node.children,
			None,
		)
		self.assertEqual(
			node.props,
			None,
		)

if __name__ == "__main__":
	unittest.main()
