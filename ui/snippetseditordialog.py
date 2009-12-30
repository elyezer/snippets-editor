# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtSnippetEditor/snippet_editor_dialog.ui'
#
# Created: Wed Dec 30 00:27:37 2009
#      by: PySide uic UI code generator
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(534, 385)
        self.gridLayout = QtGui.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 3, 1, 1)
        self.snippet_text_edit = QtGui.QPlainTextEdit(dialog)
        self.snippet_text_edit.setObjectName("snippet_text_edit")
        self.gridLayout.addWidget(self.snippet_text_edit, 1, 3, 2, 1)
        self.add_button = QtGui.QToolButton(dialog)
        self.add_button.setMinimumSize(QtCore.QSize(16, 16))
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 4, 0, 1, 1)
        self.frame = QtGui.QFrame(dialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keyword_label = QtGui.QLabel(self.frame)
        self.keyword_label.setObjectName("keyword_label")
        self.horizontalLayout.addWidget(self.keyword_label)
        self.snippet_keyword_textbox = QtGui.QLineEdit(self.frame)
        self.snippet_keyword_textbox.setObjectName("snippet_keyword_textbox")
        self.horizontalLayout.addWidget(self.snippet_keyword_textbox)
        self.gridLayout.addWidget(self.frame, 3, 3, 1, 1)
        self.remove_button = QtGui.QToolButton(dialog)
        self.remove_button.setMinimumSize(QtCore.QSize(0, 0))
        self.remove_button.setBaseSize(QtCore.QSize(16, 16))
        self.remove_button.setObjectName("remove_button")
        self.gridLayout.addWidget(self.remove_button, 4, 1, 1, 1)
        self.edit_snippet_label = QtGui.QLabel(dialog)
        self.edit_snippet_label.setObjectName("edit_snippet_label")
        self.gridLayout.addWidget(self.edit_snippet_label, 0, 3, 1, 1)
        self.snippets_tree_widget = QtGui.QTreeWidget(dialog)
        self.snippets_tree_widget.setHeaderHidden(True)
        self.snippets_tree_widget.setObjectName("snippets_tree_widget")
        self.snippets_tree_widget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.snippets_tree_widget, 0, 0, 4, 3)

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialog.reject)
        QtCore.QObject.connect(self.add_button, QtCore.SIGNAL("clicked()"), dialog.add_snippet)
        QtCore.QObject.connect(self.remove_button, QtCore.SIGNAL("clicked()"), dialog.remove_snippet)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Snippets Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.add_button.setText(QtGui.QApplication.translate("dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.keyword_label.setText(QtGui.QApplication.translate("dialog", "Keyword:", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_snippet_label.setText(QtGui.QApplication.translate("dialog", "Edit Snippet:", None, QtGui.QApplication.UnicodeUTF8))

