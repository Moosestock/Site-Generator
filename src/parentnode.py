from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)


	def to_html(self):
		if self.tag is None:
			raise ValueError("tag undefined")
		elif self.children is None:
			raise ValueError("children undefined")
		props_text = ""
		if self.props is None:
			props_text = ""
		else:
			for k, v in self.props.items():
				props_text += f' {k}"{v}"'
		child_text = ""
		for child in self.children:
			child_text += child.to_html()
		return f"<{self.tag}>{props_text}{child_text}</{self.tag}>"

	def __repr__(self):
		return f"{self. tag}, {self.value}, {self.props}" 


