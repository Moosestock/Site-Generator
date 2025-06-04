from enum import Enum
from leafnode import LeafNode
from textnode import (TextNode, TextType)

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case text_node.text_type.TEXT:
			return LeafNode(tag=None, value=text_node.text)
		case text_node.text_type.NORMAL:
			return LeafNode(tag=None, value=text_node.text)
		case text_node.text_type.BOLD:
			return LeafNode(tag="b", value=text_node.text)
		case text_node.text_type.ITALIC:
			return LeafNode(tag="i", value=text_node.text)
		case text_node.text_type.CODE:
			return LeafNode(tag="code", value=text_node.text)
		case text_node.text_type.LINK:
			return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
		case text_node.text_type.IMAGE:
			return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
		case _:
			raise Exception("Undefined TextType")
