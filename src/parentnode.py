from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)


	def to_html(self):
		if self.tag is None:
			raise ValueError("tag undefined")
		elif self.children is None:
			raise ValueError("children undefined")
#		elif self.props is None:
#			return f"<{self.tag}>{self.value}</{self.tag}>"
		print("Starting props")
		props_text = ""
		for k, v in self.props.items():
			props_text += f' {k}"{v}"'
		child_text = ""
		child_text = "".join(map(self.helper_func(child_text), self.children))
#		for child in self.children:
#			child_text = self.helper_func(child_text, child)
#		return f"<{self.tag}{props_text}{child_text}></{self.tag}>"


	def __repr__(self):
		return f"{self. tag}, {self.value}, {self.props}" 

	def helper_func(child_text, child_obj):
		return child_text + child_obj.to_html()
