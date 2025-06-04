from enum import Enum
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)


	def to_html(self):
		if self.tag is None:
			raise ValueError("invalid HTML: no tag")
		elif self.children is None:
			raise ValueError("invalid HTML: no children")
		child_text = ""
		for child in self.children:
			child_text += child.to_html()
		return f"<{self.tag}>{self.props_to_html()}{child_text}</{self.tag}>"

	def __repr__(self):
		return f"ParentNode({self. tag}, children: {self.value}, {self.props})"


