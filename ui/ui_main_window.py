from builtins import print

from PySide2 import QtCore, QtGui, QtWidgets
from ui.ui_main_window_base import Ui_MainWindowBase
import config.config_loader as config_loader
from PySide2.QtWidgets import QFileDialog
import yaml
from PySide2.QtCore import QObject
import sys, os
from pathlib import Path

class Ui_MainWindow(Ui_MainWindowBase):

    def update_window_config(self):
        self.configFilePath.clicked.connect(lambda: self.__loadConfig(self.config_File_name, "*.yml"))
        self.save.clicked.connect(self.__save)
        self.privateKeyPath.clicked.connect(lambda:self.__setFilePath(self.private_key_file, "*.key"))
        self.userListFilePath.clicked.connect(lambda:self.__setFilePath(self.users_filename, "*.csv"))

    def __loadConfig(self, field: QtWidgets.QLineEdit, fileType):
        self.message.setText("")
        self.message.setStyleSheet('background-color : #fff;')
        self.__setFilePath(field, fileType)
        if field.text():
            field.setText(field.text())
            self.setDefaultValues(field.text())

    def __setFilePath(self, field: QtWidgets.QLineEdit, fileType):
        directoryPath = Path(__file__).parents[2]
        path_to_file, _ = QFileDialog.getOpenFileName(None,"Load File Path",directoryPath.__str__(),fileType,None)
        field.setText(path_to_file)


    def __save(self):
        fileName = None
        if self.config_File_name.text() is not None and  not self.config_File_name:
            fileName = self.config_File_name.text()
            config = yaml.load(open(fileName))
        else:
            parentPath = Path(__file__).parents[2]
            fileName = parentPath.__str__()+'/user-config.yml'
            self.config_File_name.setText(fileName)
            data = dict(
                configuration=dict(),
                umapi = dict()
            )
            yaml.dump(data, open(fileName, "w+"), default_flow_style=False)
            config = yaml.load(open(fileName))


        umapi = config["umapi"]
        umapi["org_id"] = self.org_id.text()
        umapi["tech_acct_id"] = self.tech_acct_id.text()
        umapi["api_key"] = self.api_key.text()
        umapi["client_secret"] = self.client_secret.text()
        umapi["private_key_file"] = self.private_key_file.text()
        umapi["host"] = self.host.text()
        umapi["ims_host"] = self.ims_host.text()

        configuration = config["configuration"]
        configuration["id_type"] = self.id_type.text()
        configuration["logon_type"] = self.logon_type.text()
        configuration["username_file"] = self.users_filename.text()

        yaml.dump(config, open(fileName, "w"), default_flow_style=False)

    def setDefaultValues(self, configFile):
        try:
            umapi, config = config_loader.ConfigLoader().load_config(config_filename=configFile)
            self.org_id.setText(umapi.org_id)
            self.tech_acct_id.setText(umapi.tech_acct_id)
            self.api_key.setText(umapi.api_key)
            self.client_secret.setText(umapi.client_secret)
            self.host.setText(umapi.host)
            self.ims_host.setText(umapi.ims_host)
            self.private_key_file.setText(umapi.private_key_file)
            self.id_type.setText(config.id_type)
            self.logon_type.setText(config.logon_type)
            self.users_filename.setText(config.users_filename)
        except TypeError:
            self.message.setText("  Error: Invalid config file")
            self.message.setStyleSheet('background-color : #f8d7da; color : #E60000; ')

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(590, 561)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label.setStyleSheet('background-color : #838383; color : #fff;')
    ui.label_2.setStyleSheet('background-color : #838383; color : #fff;')
    ui.label_4.setStyleSheet('background-color : #838383; color : #fff;')
    ui.update_window_config()
    MainWindow.show()
    sys.exit(app.exec_())

