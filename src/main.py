from textnode import (TextNode, TextType)
from htmlnode import HTMLNode
from splitnode import *
from markdown_blocks import *
from markdown_blocks import *

def main():

	print(block_to_block_type("1: This is a heading"))
	print(block_to_block_type("``` 1. Tis is code ```"))
	print(block_to_block_type(">``` 1. This is a quote ```"))
	print(block_to_block_type("- ``` > 1. This is an ordered list ```"))
	print(block_to_block_type("->``` 1. This is an unordered list ```"))


main()
