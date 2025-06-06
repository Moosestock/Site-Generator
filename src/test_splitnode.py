import unittest
from enum import Enum
from splitnode import *
from textnode import TextNode, TextType


class TestSplitNodeDelimiter(unittest.TestCase):
	def test_split_node_bold_and_italics(self):
		test_node = TextNode("This is **bold text ** and this is* italic text* so ...", TextType.TEXT)
		is_equal = "Huh?"
		bold_nodes = split_node_delimiter([test_node], "**", TextType.BOLD)
		italic_nodes = split_node_delimiter(bold_nodes, "*", TextType.ITALIC)
		expected_list = [TextNode("This is ", TextType.TEXT, None), TextNode("bold text ", TextType.BOLD, None), TextNode(" and this is", TextType.TEXT, None), TextNode(" italic text", TextType.ITALIC, None), TextNode(" so ...", TextType.TEXT, None)]
		self.assertEqual(italic_nodes, expected_list)

	def test_split_node_empty(self):
		test_node = TextNode("", TextType.TEXT)
		bold_nodes = split_node_delimiter([test_node], "**", TextType.BOLD)
		italic_nodes = split_node_delimiter(bold_nodes, "*", TextType.ITALIC)

	def test_delim_bold(self):
		node = TextNode("This is text with a **bolded** word", TextType.TEXT)
		new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_double(self):
		node = TextNode(
			"This is text with a **bolded** word and **another**", TextType.TEXT
		)
		new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_bold_multiword(self):
		node = TextNode(
			"This is text with a **bolded word** and **another**", TextType.TEXT
		)
		new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded word", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_italic(self):
		node = TextNode("This is text with an _italic_ word", TextType.TEXT)
		new_nodes = split_node_delimiter([node], "_", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_node_delimiter([node], "`", TextType.CODE)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			"This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
		)
		self.assertListEqual(
			[
				("link", "https://boot.dev"),
				("another link", "https://blog.boot.dev"),
			],
			matches,
		)

	def test_split_image(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
			TextType.TEXT,
		)
		new_nodes = split_node_images([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes,
		)

	def test_split_image_single(self):
		node = TextNode(
			"![image](https://www.example.COM/IMAGE.PNG)",
			TextType.TEXT,
		)
		new_nodes = split_node_images([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
			],
			new_nodes,
		)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_node_images([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
		TextType.TEXT,
		)
		new_nodes = split_node_links([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
				TextNode(" and ", TextType.TEXT),
				TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
				TextNode(" with text that follows", TextType.TEXT),
			],
			new_nodes,
		)

	def test_text_to_textnodes(self):
		test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		split_nodes = text_to_textnodes(test_text)
		self.assertListEqual(
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.TEXT),
				TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			],
			split_nodes,
		)


