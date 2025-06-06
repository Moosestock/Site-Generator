from enum import Enum
from parentnode import ParentNode
from textnode import TextNode, TextType
from splitnode import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node

class BlockType(Enum):
	PARAGRAPH = "p"
	HEADING = "h" # <h1> - <h6> depending on the level
	CODE = "code"
	QUOTE = "blockquote"
	ULIST = "ul" # each list item is surrounded by "<li>"
	OLIST = "ol" # surround each item with "<li>"

def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	filtered_blocks = []
	for block in blocks:
		if block == "":
			continue
		block = block.strip()
		filtered_blocks.append(block)
	return filtered_blocks

def block_to_block_type(block):
	blocks = block.split("\n")

	if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING
	if len(blocks) > 1 and blocks[0].startswith("```") and blocks[-1].startswith("```"):
		return BlockType.CODE
	if block.startswith(">"):
		for bluk in blocks:
			if not bluk.startswith(">"):
				return BlockType.PARAGRAPH
		return BlockType.QUOTE
	if block.startswith("- "):
		for bluk in blocks:
			if not bluk.startswith("- "):
				return BlockType.PARAGRAPH
		return BlockType.ULIST
	if block.startswith("1. "):
		i = 1
		for bluk in blocks:
			if not bluk.startswith(f"{i}. "):
				return BlockType.PARAGRAPH
			i += 1
		return BlockType.OLIST
	return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	children = []
	for block in blocks:
		html_node = block_to_html_node(block)
		children.append(html_node)
	return ParentNode("div", children, None)
	
def block_to_html_node(block):
	block_type = block_to_block_type(block)
	match block_type:
		case BlockType.PARAGRAPH:
			return paragraph_to_html_node(block)
		case BlockType.HEADING:
			return heading_to_html_node(block)
		case BlockType.CODE:
			return code_to_html_node(block)
		case BlockType.QUOTE:
			return quote_to_html_node(block)
		case BlockType.OLIST:
			return olist_to_html_node(block)
		case BlockType.ULIST:
			return ulist_to_html_node(block)
		case _:
			return ValueError("Invalid block type")

def text_to_children(text):
	dez_nodes = text_to_textnodes(text) # get nodes from block text
	those_nodes = []
	for node in dez_nodes:
		those_nodes.append(text_node_to_html_node(node))
	return those_nodes

def paragraph_to_html_node(block):
	split_text = block.split("\n")
	new_text = " ".join(split_text)
	kids = text_to_children(new_text)
	return ParentNode(tag="p", children=kids, props=None)

def heading_to_html_node(block):
	level = 0
	for char in block:
		if char == "#":
			level += 1
		else:
			break
	if level + 1 >= len(block):
		raise ValueError(f"invalid heading level: {level}")
	text = block[level+1:]
	children = text_to_children(text)
	return ParentNode(f"h{level}", children)


def code_to_html_node(block):
	if not block.startswith("```") or not block.endswith("```"):
		raise ValueError("Invalid code block")
	text = block[4: -3]
	raw_text_node = TextNode(text, TextType.TEXT)
	child = text_node_to_html_node(raw_text_node)
	code = ParentNode("code", [child])
	return ParentNode("pre", [code])

def olist_to_html_node(block):
	items = block.split("\n")
	html_items = []
	for item in items:
		text = item[3:]
		children = text_to_children(text)
		html_items.append(ParentNode("li", children))
	return ParentNode("ol", html_items)

def ulist_to_html_node(block):
	items = block.split("\n")
	html_items = []
	for item in items:
		text = item[2:]
		children = text_to_children(text)
		html_items.append(ParentNode("li", children))
	return ParentNode("ul", html_items)

def quote_to_html_node(block):
	lines = block.split("\n")
	new_lines = []
	for line in lines:
		if not line.startswith(">"):
			raise ValueError("Invalid qutoe block")
		new_lines.append(line.lstrip(">".strip()))
	content = " ".join(new_lines)
	children = text_to_children(content)
	return ParentNode("blockquote", children)



