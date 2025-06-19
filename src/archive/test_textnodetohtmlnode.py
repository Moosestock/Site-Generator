import unittest
from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import (TextNode, TextType)
from textnodetohtmlnode import text_node_to_html_node

class TestTextNodetoHTMLNode(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("This is a bold node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a bold node")

	def test_italic(self):
		node = TextNode("This is an italic node", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is an italic node")

	def test_code(self):
		node = TextNode("This is a code node", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a code node")

	def test_link(self):
		node = TextNode("This is a link node", TextType.LINK, "https://www.boot.it")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a link node")
		self.assertEqual(html_node.props, {'href': 'https://www.boot.it'})

	def test_image(self):
		node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.it")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {'src': 'https://www.boot.it', 'alt': 'This is an image node'})

	def test_exception(self):
		with self.assertRaises(Exception):
			node = TextNode("This has no text type")

if __name__ == "__main__":
	unittest.main()
