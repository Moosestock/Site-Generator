import unittest
from enum import Enum
from splitnode import split_node_delimiter
from textnode import TextNode, TextType


class TestSplitNodeDelimiter(unittest.TestCase):
	def test_split_node_bold_and_italics(self):
		test_node = TextNode("This is **bold text ** and this is* italic text* so ...", TextType.TEXT)
		is_equal = "Huh?"
		bold_nodes = split_node_delimiter([test_node], "**", TextType.BOLD)
		italic_nodes = split_node_delimiter(bold_nodes, "*", TextType.ITALIC)
		self.maxDiff = None
		self.assertEqual(repr(italic_nodes), "[TextNode(This is , TextType.TEXT, None), TextNode(bold text , TextType.BOLD, None), TextNode( and this is, TextType.TEXT, None), TextNode( italic text, TextType.ITALIC, None), TextNode( so ..., TextType.TEXT, None)]")
