from textnode import (TextNode, TextType)
from htmlnode import HTMLNode
from splitnode import split_node_delimiter
from extractimages import extract_markdown_images, extract_markdown_links

def main():
#	print(TextNode("this is the txt", TextType.LINK, "https://www.boot.dev"))
#	print(HTMLNode("This is a tag", "This is the value", "List of children = None", "PROPS!"))

#	a_node = TextNode("This is **bold** with *italic* texts", TextType.TEXT)
#	print(repr(a_node))

#	split_bold = split_node_delimiter([a_node], "**", TextType.BOLD)
#	print(repr(split_bold))

#	split_italic = split_node_delimiter(split_bold, "*", TextType.ITALIC)
#	print(repr(split_italic))

	test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
	print(extract_markdown_images(test_text))

	test_text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
	print(extract_markdown_links(test_text2))

main()
