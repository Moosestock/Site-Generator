import unittest
from extractimages import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
	def test_extract_markdown_images(self):
		test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		image_list = extract_markdown_images(test_text)
		expected_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
		self.assertEqual(image_list, expected_list)

	def test_extract_markdown_images_empty(self):
		test_text = ""
		image_list = extract_markdown_images(test_text)
		expected_list = [] 
		self.assertEqual(image_list, expected_list)

	def test_extract_markdown_links(self):
		test_text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		link_list = extract_markdown_links(test_text2)
		print(link_list)
		expected_list = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
		self.assertEqual(link_list, expected_list)

	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
	    )
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
