from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)
		if self.value is None:
			raise ValueError

	def to_html(self):
		if self.value is None:
			raise ValueError
		if self.tag is None:
			return self.value
		elif self.props is None:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		url_text = ""
		for k, v in self.props.items():
			url_text += f' {k}="{v}"'
		return f"<{self.tag}{url_text}>{self.value}</{self.tag}>"
	
	def __repr__(self):
		return f"{self. tag}, {self.value}, {self.props}" 

