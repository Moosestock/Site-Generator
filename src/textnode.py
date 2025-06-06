from enum import Enum

class TextType(Enum):
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code" # code needs to be nested inside a "<pre>" tag, e.g. <pre><code>
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return self.text == target.text and \
        self.text_type == target.text_type and \
        self.url == target.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

