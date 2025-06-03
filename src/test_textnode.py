import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_repr(self):
		text_in = ("This is more text, blah, blah, blah...")
		text_type = TextType.CODE
		url = "https://suckittrebek.com"
		node = TextNode(text_in, text_type, url)
		node2 = f"TextNode({text_in}, {text_type.value}, {url})"
		self.assertEqual(repr(node), node2)

	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.IMAGE)
		self.assertNotEqual(node, node2)

	def test_exception(self):
		with self.assertRaises(AttributeError):
			TextNode("This is an test of the emergency Exception system. This is only a test.", TextType.Trouble)

if __name__ == "__main__":
	unittest.main()
