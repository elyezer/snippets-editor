from PySide import QtGui, QtCore
from models.snippetsmodel import SnippetFileReader
from ui.snippetseditordialog import Ui_dialog
from ui.snippetseditor import SnippetItem

class SnippetDialog(QtGui.QDialog, Ui_dialog):
    def __init__(self):
        super(SnippetDialog, self).__init__()
        self.setupUi(self)
        self.snippet_text_edit.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
        QtCore.QObject.connect(self.snippets_tree_widget, QtCore.SIGNAL("itemSelectionChanged()"), self.itemSelectionChanged)
    
    def itemSelectionChanged(self):
        selected = self.snippets_tree_widget.selectedItems()[0]
        if isinstance(selected, SnippetItem):
            self.snippet_text_edit.setPlainText(selected.body)
            self.snippet_keyword_textbox.setText(selected.keyword)
        
    
    def add_snippet(self):
        item = self.get_selected_item()
        
        new_snippet = SnippetItem("", "", "")
        new_snippet.setText(0, "Untitled")
        
        item.addChild(new_snippet)
        
        if not item.isExpanded():
            item.setExpanded(True)
    
    def remove_snippet(self):
        item = self.get_selected_item()
        item.removeChild(self.snippets_tree_widget.selectedItems()[0])
    
    def get_selected_item(self):
        item = self.snippets_tree_widget.selectedItems()[0]
        
        if item.parent() != None:
            item = item.parent()
        
        return item
    
    def add_items(self):
        languages = ["c", "html", "python", "ruby", "xml"]
        for language in languages:    
            snippet_reader = SnippetFileReader(path="languages/%s/snippets.xml" % language)
            snippets = snippet_reader.get_contents().getiterator("snippet")
            language_item = QtGui.QTreeWidgetItem(self.snippets_tree_widget)
            language_item.setText(0, language.title())
            for snippet in snippets:
                snippet_item = SnippetItem()
                snippet_item.body = snippet.find("body").text
                snippet_item.keyword = snippet.find("key").text
                snippet_item.name = snippet.find("name").text
                snippet_item.setText(0, snippet_item.name)
                language_item.addChild(snippet_item)
    
