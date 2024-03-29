#!/usr/bin/env python3
from pyqode.qt import QtWidgets
from gnucobolide.view.forms import dlg_cobc_help_ui


class DlgCobcHelp(QtWidgets.QDialog):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.ui = dlg_cobc_help_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.plainTextEdit.setPlainText(text)