# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_2D_sweep.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create2DSweep(object):
    def setupUi(self, Create2DSweep):
        Create2DSweep.setObjectName("Create2DSweep")
        Create2DSweep.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Create2DSweep)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Create2DSweep)
        self.buttonBox.accepted.connect(Create2DSweep.accept) # type: ignore
        self.buttonBox.rejected.connect(Create2DSweep.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Create2DSweep)

    def retranslateUi(self, Create2DSweep):
        _translate = QtCore.QCoreApplication.translate
        Create2DSweep.setWindowTitle(_translate("Create2DSweep", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Create2DSweep = QtWidgets.QDialog()
    ui = Ui_Create2DSweep()
    ui.setupUi(Create2DSweep)
    Create2DSweep.show()
    sys.exit(app.exec_())