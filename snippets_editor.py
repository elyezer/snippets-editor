from PySide import QtGui, QtCore
from snippets_editor_dialog import Ui_dialog
import sys

class SnippetDialog(QtGui.QDialog, Ui_dialog):
    def __init__(self):
        super(SnippetDialog, self).__init__()
    
    def selectionChanged(self, selected, deselected):
        print selected
    
    def add_snippet(self):
        item = self.get_selected_item()
        
        new_snippet = QtGui.QTreeWidgetItem()
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

def add_items(snippets_tree_widget):
    c = QtGui.QTreeWidgetItem(snippets_tree_widget)
    c.addChild(QtGui.QTreeWidgetItem())
    QtGui.QTreeWidgetItem(snippets_tree_widget)
    QtGui.QTreeWidgetItem(snippets_tree_widget)
    
    snippets_tree_widget.topLevelItem(0).setText(0, "C")
    snippets_tree_widget.topLevelItem(0).child(0).setText(0, "main")
    snippets_tree_widget.topLevelItem(1).setText(0, "Python")
    snippets_tree_widget.topLevelItem(2).setText(0, "Ruby")

def main(argv):
    application = QtGui.QApplication(argv)
    dialog = SnippetDialog()
    dialog.setupUi(dialog)
    
    dialog.snippets_tree_widget.selectionChanged = dialog.selectionChanged
    
    add_items(dialog.snippets_tree_widget)
    
    dialog.show()
    
    sys.exit(application.exec_())

if __name__ == '__main__':
    main(sys.argv)