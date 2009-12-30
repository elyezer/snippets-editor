from PySide.QtGui import QTreeWidgetItem

class SnippetItem(QTreeWidgetItem):
    """This class represents a snippet item in the tree widget"""
    def __init__(self, body=None, keyword=None, name=None):
        super(SnippetItem, self).__init__()
        self.body = body
        self.keyword = keyword
        self.name = name
    
