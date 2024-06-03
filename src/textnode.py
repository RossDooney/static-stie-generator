class TextNode:
    def __init__(self, text="", text_type="", url=""):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textNodeNew):
        return (
            self.text_type == textNodeNew.text_type
            and self.text == textNodeNew.text
            and self.url == textNodeNew.url
        )

    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"