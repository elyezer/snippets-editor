from xml.etree.ElementTree import ElementTree

class SnippetFileReader(ElementTree):
    def __init__(self, path=None):
        self.path = path
    
    def get_contents(self):
        """Get the contents from a snippet file"""
        if self.path != None:
            return self.parse(self.path)
        else:
            return None
    
