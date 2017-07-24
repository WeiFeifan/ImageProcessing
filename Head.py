# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiemian1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(742, 551)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 80, 20, 261))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(440, 80, 20, 261))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.process = QtGui.QPushButton(self.centralwidget)
        self.process.setGeometry(QtCore.QRect(330, 290, 93, 28))
        self.process.setObjectName(_fromUtf8("process"))
        self.Gauss = QtGui.QRadioButton(self.centralwidget)
        self.Gauss.setGeometry(QtCore.QRect(330, 90, 115, 19))
        self.Gauss.setObjectName(_fromUtf8("Gauss"))
        self.Mean = QtGui.QRadioButton(self.centralwidget)
        self.Mean.setGeometry(QtCore.QRect(330, 130, 115, 19))
        self.Mean.setObjectName(_fromUtf8("Mean"))
        self.Median = QtGui.QRadioButton(self.centralwidget)
        self.Median.setGeometry(QtCore.QRect(330, 170, 115, 19))
        self.Median.setObjectName(_fromUtf8("Median"))
        self.Laplace = QtGui.QRadioButton(self.centralwidget)
        self.Laplace.setGeometry(QtCore.QRect(330, 250, 115, 19))
        self.Laplace.setObjectName(_fromUtf8("Laplace"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 256, 271))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(480, 80, 256, 271))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.open = QtGui.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(70, 380, 93, 28))
        self.open.setObjectName(_fromUtf8("open"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 50, 101, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Gradient = QtGui.QRadioButton(self.centralwidget)
        self.Gradient.setGeometry(QtCore.QRect(330, 210, 115, 19))
        self.Gradient.setObjectName(_fromUtf8("Gradient"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(540, 380, 151, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.line.raise_()
        self.line_2.raise_()
        self.process.raise_()
        self.Gauss.raise_()
        self.Mean.raise_()
        self.Median.raise_()
        self.Laplace.raise_()
        self.open.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.Gradient.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.fileOpen = QtGui.QAction(MainWindow)
        self.fileOpen.setObjectName(_fromUtf8("fileOpen"))
        self.fileShut = QtGui.QAction(MainWindow)
        self.fileShut.setObjectName(_fromUtf8("fileShut"))
        self.menu.addAction(self.fileOpen)
        self.menu.addAction(self.fileShut)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

#两个button的connect，
        self.open.clicked.connect(MainWindow.openimage)
        self.process.clicked.connect(MainWindow.processing)
#radiobutton的connect
        self.Gauss.toggled.connect(MainWindow.flagGauss)
        self.Mean.toggled.connect(MainWindow.flagMean)
        self.Laplace.toggled.connect(MainWindow.flagLaplace)
        self.Median.toggled.connect(MainWindow.flagMedian)
        self.Gradient.toggled.connect(MainWindow.flagGradient)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.process.setText(_translate("MainWindow", "运行", None))
        self.Gauss.setText(_translate("MainWindow", "Gauss", None))
        self.Mean.setText(_translate("MainWindow", "Mean", None))
        self.Median.setText(_translate("MainWindow", "Median", None))
        self.Laplace.setText(_translate("MainWindow", "Laplace", None))
        self.open.setText(_translate("MainWindow", "打开图片", None))
        self.label.setText(_translate("MainWindow", "原始图像", None))
        self.label_2.setText(_translate("MainWindow", "处理后图像", None))
        self.Gradient.setText(_translate("MainWindow", "Gradient", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "编辑", None))
        self.menu_3.setTitle(_translate("MainWindow", "关于", None))
        self.fileOpen.setText(_translate("MainWindow", "打开", None))
        self.fileShut.setText(_translate("MainWindow", "关闭", None))

