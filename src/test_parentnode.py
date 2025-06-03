import unittest

from parentnode import ParentNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, world!", {"href": "https://www.moosespot.ca"})
		compare_text = "<a href=\"https://www.moosespot.ca\">Hello, world!</a>"
		self.assertEqual(node.to_html(), compare_text)

	def test_repr(self):
		node = LeafNode("p", "Hello, world!")
		node2 = "p, Hello, world!, None"
		self.assertEqual(repr(node), node2)

	def test_exception(self):
		with self.assertRaises(TypeError):
			LeafNode("p")

if __name__ == "__main__":
	unittest.main()
