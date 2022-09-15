# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_inter(object):
    def setupUi(self, MainWindow_inter):
        MainWindow_inter.setObjectName("MainWindow_inter")
        MainWindow_inter.resize(714, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow_inter)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(56, 57, 60);\n"
"border:1px;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(86, 88, 93);\n"
"    border:1px;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
" \n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_maxsize = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_maxsize.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border-bottom:5px;\n"
"    background-color: rgb(115, 115, 115);\n"
"\n"
"}")
        self.pushButton_maxsize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/1-最大化-_2_.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_maxsize.setIcon(icon)
        self.pushButton_maxsize.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_maxsize.setObjectName("pushButton_maxsize")
        self.horizontalLayout_2.addWidget(self.pushButton_maxsize)
        self.pushButton_minsize = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_minsize.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border-bottom:5px;\n"
"    background-color: rgb(115, 115, 115);\n"
"\n"
"}")
        self.pushButton_minsize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/最小化.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minsize.setIcon(icon1)
        self.pushButton_minsize.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_minsize.setObjectName("pushButton_minsize")
        self.horizontalLayout_2.addWidget(self.pushButton_minsize)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border-bottom:5px;\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/关闭.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setToolTipDuration(0)
        self.treeWidget.setStyleSheet("#treeWidget{\n"
"    background-color: rgb(77, 79, 83);\n"
"    border:1px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QHeaderView::section{  color:white; height:30px; border:none; background-color: rgb(77, 79, 83);}\n"
"")
        self.treeWidget.setLineWidth(0)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/wxb主页.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon3)
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(0, 0, 0))
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_1.setFont(0, font)
        self.horizontalLayout_4.addWidget(self.treeWidget)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("border:1px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(17)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow_inter.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_inter)
        self.pushButton_2.clicked.connect(MainWindow_inter.close)
        self.pushButton_minsize.clicked.connect(MainWindow_inter.showMinimized)
        self.pushButton_maxsize.clicked.connect(MainWindow_inter.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_inter)

    def retranslateUi(self, MainWindow_inter):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_inter.setWindowTitle(_translate("MainWindow_inter", "MainWindow"))
        self.label.setText(_translate("MainWindow_inter", "HEPS 微振动监测系统"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow_inter", "导航"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow_inter", "数据"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow_inter", "东方采集仪"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow_inter", "提取数据"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow_inter", "转换数据"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow_inter", "绘图"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow_inter", "时域信号"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow_inter", "位移RMS积分"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow_inter", "数据重叠对比"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow_inter", "计算"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow_inter", "相关性计算"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow_inter", "互谱计算"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow_inter", "传递函数计算"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow_inter", "其他"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow_inter", "..."))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
import res_rc
