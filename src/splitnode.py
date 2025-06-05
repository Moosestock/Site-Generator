from enum import Enum
from textnode import TextNode, TextType


def split_node_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	debug_counter = 0
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			new_node_list = []
			node_text = node.text.split(delimiter)
			if len(node_text) == 1 and node_text[0] != delimiter:
				new_node_list.append(node)
			elif (len(node_text) == 1 and node_text[0] == delimiter) or len(node_text) % 2 == 0:
				raise Exception("hey! what are you trying to pull?")
			else:
				i = 0
				for block_text in node_text:
					if i % 2 == 0:
						new_node_list.append(TextNode(block_text, TextType.TEXT))
					else:
						new_node_list.append(TextNode(block_text, text_type))
					i += 1
			new_nodes.extend(new_node_list)
	return new_nodes

