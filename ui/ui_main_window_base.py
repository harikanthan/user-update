# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(681, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 681, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.save = QtWidgets.QPushButton(self.tab)
        self.save.setGeometry(QtCore.QRect(500, 460, 75, 23))
        self.save.setObjectName("save")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 511, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.config_File_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.config_File_name.setObjectName("config_File_name")
        self.verticalLayout_7.addWidget(self.config_File_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.configFilePath = QtWidgets.QToolButton(self.layoutWidget)
        self.configFilePath.setObjectName("configFilePath")
        self.verticalLayout_8.addWidget(self.configFilePath)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.message = QtWidgets.QLabel(self.tab)
        self.message.setGeometry(QtCore.QRect(100, 20, 401, 21))
        self.message.setText("")
        self.message.setObjectName("message")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(60, 100, 511, 216))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.organizationIDLabel = QtWidgets.QLabel(self.widget)
        self.organizationIDLabel.setObjectName("organizationIDLabel")
        self.verticalLayout.addWidget(self.organizationIDLabel)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.org_id = QtWidgets.QLineEdit(self.widget)
        self.org_id.setObjectName("org_id")
        self.verticalLayout_2.addWidget(self.org_id)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.technicalAccountIDLabel = QtWidgets.QLabel(self.widget)
        self.technicalAccountIDLabel.setObjectName("technicalAccountIDLabel")
        self.verticalLayout_4.addWidget(self.technicalAccountIDLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tech_acct_id = QtWidgets.QLineEdit(self.widget)
        self.tech_acct_id.setObjectName("tech_acct_id")
        self.verticalLayout_5.addWidget(self.tech_acct_id)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 2, 1, 1)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.aPIKeyClientIDLabel = QtWidgets.QLabel(self.widget)
        self.aPIKeyClientIDLabel.setObjectName("aPIKeyClientIDLabel")
        self.verticalLayout_25.addWidget(self.aPIKeyClientIDLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_25, 2, 0, 1, 1)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.api_key = QtWidgets.QLineEdit(self.widget)
        self.api_key.setObjectName("api_key")
        self.verticalLayout_26.addWidget(self.api_key)
        self.gridLayout_2.addLayout(self.verticalLayout_26, 2, 1, 1, 1)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.gridLayout_2.addLayout(self.verticalLayout_27, 2, 2, 1, 1)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.clientSecretLabel = QtWidgets.QLabel(self.widget)
        self.clientSecretLabel.setObjectName("clientSecretLabel")
        self.verticalLayout_28.addWidget(self.clientSecretLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_28, 3, 0, 1, 1)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.client_secret = QtWidgets.QLineEdit(self.widget)
        self.client_secret.setObjectName("client_secret")
        self.verticalLayout_29.addWidget(self.client_secret)
        self.gridLayout_2.addLayout(self.verticalLayout_29, 3, 1, 1, 1)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.gridLayout_2.addLayout(self.verticalLayout_30, 3, 2, 1, 1)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.hostLabel = QtWidgets.QLabel(self.widget)
        self.hostLabel.setObjectName("hostLabel")
        self.verticalLayout_31.addWidget(self.hostLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_31, 4, 0, 1, 1)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.host = QtWidgets.QLineEdit(self.widget)
        self.host.setObjectName("host")
        self.verticalLayout_32.addWidget(self.host)
        self.gridLayout_2.addLayout(self.verticalLayout_32, 4, 1, 1, 1)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.gridLayout_2.addLayout(self.verticalLayout_33, 4, 2, 1, 1)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.imsHostLabel = QtWidgets.QLabel(self.widget)
        self.imsHostLabel.setObjectName("imsHostLabel")
        self.verticalLayout_34.addWidget(self.imsHostLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_34, 5, 0, 1, 1)
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.ims_host = QtWidgets.QLineEdit(self.widget)
        self.ims_host.setObjectName("ims_host")
        self.verticalLayout_35.addWidget(self.ims_host)
        self.gridLayout_2.addLayout(self.verticalLayout_35, 5, 1, 1, 1)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.gridLayout_2.addLayout(self.verticalLayout_36, 5, 2, 1, 1)
        self.verticalLayout_37 = QtWidgets.QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.privateKeyFileLabel = QtWidgets.QLabel(self.widget)
        self.privateKeyFileLabel.setObjectName("privateKeyFileLabel")
        self.verticalLayout_37.addWidget(self.privateKeyFileLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_37, 6, 0, 1, 1)
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.private_key_file = QtWidgets.QLineEdit(self.widget)
        self.private_key_file.setObjectName("private_key_file")
        self.verticalLayout_38.addWidget(self.private_key_file)
        self.gridLayout_2.addLayout(self.verticalLayout_38, 6, 1, 1, 1)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.privateKeyPath = QtWidgets.QToolButton(self.widget)
        self.privateKeyPath.setObjectName("privateKeyPath")
        self.verticalLayout_39.addWidget(self.privateKeyPath)
        self.gridLayout_2.addLayout(self.verticalLayout_39, 6, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(60, 330, 511, 98))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.logon_type = QtWidgets.QLineEdit(self.widget1)
        self.logon_type.setObjectName("logon_type")
        self.gridLayout.addWidget(self.logon_type, 1, 1, 1, 1)
        self.id_type = QtWidgets.QLineEdit(self.widget1)
        self.id_type.setObjectName("id_type")
        self.gridLayout.addWidget(self.id_type, 0, 1, 1, 1)
        self.idTypeLabel = QtWidgets.QLabel(self.widget1)
        self.idTypeLabel.setObjectName("idTypeLabel")
        self.gridLayout.addWidget(self.idTypeLabel, 0, 0, 1, 1)
        self.logonTypeLabel = QtWidgets.QLabel(self.widget1)
        self.logonTypeLabel.setObjectName("logonTypeLabel")
        self.gridLayout.addWidget(self.logonTypeLabel, 1, 0, 1, 1)
        self.userNameFileLabel = QtWidgets.QLabel(self.widget1)
        self.userNameFileLabel.setObjectName("userNameFileLabel")
        self.gridLayout.addWidget(self.userNameFileLabel, 2, 0, 1, 1)
        self.users_filename = QtWidgets.QLineEdit(self.widget1)
        self.users_filename.setObjectName("users_filename")
        self.gridLayout.addWidget(self.users_filename, 2, 1, 1, 1)
        self.userListFilePath = QtWidgets.QToolButton(self.widget1)
        self.userListFilePath.setObjectName("userListFilePath")
        self.gridLayout.addWidget(self.userListFilePath, 2, 2, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName("menubar")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "Admin Console User Update Tool"))
        self.save.setText(_translate("MainWindowBase", "Save"))
        self.label_3.setText(_translate("MainWindowBase", "Configuration File    "))
        self.configFilePath.setText(_translate("MainWindowBase", "..."))
        self.label.setText(_translate("MainWindowBase", "UMAPI Configurations"))
        self.organizationIDLabel.setText(_translate("MainWindowBase", "Organization ID"))
        self.technicalAccountIDLabel.setText(_translate("MainWindowBase", "Technical account ID"))
        self.aPIKeyClientIDLabel.setText(_translate("MainWindowBase", "API Key (Client ID)"))
        self.clientSecretLabel.setText(_translate("MainWindowBase", "Client secret"))
        self.hostLabel.setText(_translate("MainWindowBase", "Host"))
        self.imsHostLabel.setText(_translate("MainWindowBase", "ims Host"))
        self.privateKeyFileLabel.setText(_translate("MainWindowBase", "Private Key File"))
        self.privateKeyPath.setText(_translate("MainWindowBase", "..."))
        self.label_2.setText(_translate("MainWindowBase", "User Configurations"))
        self.idTypeLabel.setText(_translate("MainWindowBase", "Id Type"))
        self.logonTypeLabel.setText(_translate("MainWindowBase", "Logon Type"))
        self.userNameFileLabel.setText(_translate("MainWindowBase", "User Name File  "))
        self.userListFilePath.setText(_translate("MainWindowBase", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowBase", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowBase", "Update Users"))