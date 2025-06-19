from leafnode import LeafNode
from parentnode import ParentNode

node = LeafNode("p", "hello world!", {"href": "https://www.suck.it"})

child_node = LeafNode(tag="span", value="child", props={"props": "text"})
parent_node = ParentNode(tag="div", children=[child_node], props={"This is": "props"})


