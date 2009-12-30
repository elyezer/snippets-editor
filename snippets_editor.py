from PySide import QtGui
from controllers.snippetseditor import SnippetDialog
import sys

def main(argv):
    application = QtGui.QApplication(argv)
    
    dialog = SnippetDialog()
    dialog.add_items()
    dialog.show()
    
    sys.exit(application.exec_())

if __name__ == '__main__':
    main(sys.argv)