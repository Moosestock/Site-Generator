import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_children_and_props(self):
		child_node = LeafNode("span", "child", {"Prop": "S"})
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), '<div><span Prop="S">child</span></div>')

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_dinks(self):
		parent_node = ParentNode("div", {})
		self.assertEqual(parent_node.to_html(), "<div></div>")
	
	def test_to_html_with_ValueError_no_children(self):
		with self.assertRaises(ValueError):
			parent_node = ParentNode("div", None)
			print(parent_node.to_html())

	def test_to_html_with_ValueError_no_tag(self):
		with self.assertRaises(ValueError):
			parent_node = ParentNode(None, {})
			print(parent_node.to_html())

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_many_children(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
		)

	def test_headings(self):
		node = ParentNode(
			"h2",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			"<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
		)

if __name__ == "__main__":
	unittest.main()
