import os
import sys
from os import path
from pathlib import Path

import yaml
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QPalette
import config.config_loader as config_loader
from ui.ui_main_window_base import Ui_MainWindowBase
from PySide2.QtCore import Qt
import subprocess


class Ui_MainWindow(Ui_MainWindowBase):
    ERROR_MESSAGE_STYLE = 'background-color : #f8d7da; color : #E60000; '
    SUCCESS_MESSAGE_STYLE = 'background-color : #dff0d8; color : #126931; '
    GREY_CARD_TILE= 'background-color : #838383; color : #fff;'
    WHITE_BACKGROUND = 'background-color : #fff;'

    def update_window_config(self):
        self.configFilePath.clicked.connect(lambda: self.__loadConfig(self.config_File_name, "*.yml"))
        self.save.clicked.connect(self.__save)
        self.privateKeyPath.clicked.connect(lambda: self.__setFilePath(self.private_key_file, "*.key"))
        self.userListFilePath.clicked.connect(lambda: self.__setFilePath(self.users_filename, "*.csv"))
        self.run_user_update.clicked.connect(self.__run_user_update)

        self.config_File_name_readOnly.setReadOnly(True)
        self.grey = QPalette()
        self.grey.setColor(QPalette.Base, Qt.lightGray)
        self.grey.setColor(QPalette.Text, Qt.black)
        self.config_File_name_readOnly.setPalette(self.grey)

        # Rename label_x
        self.label.setStyleSheet(self.GREY_CARD_TILE)
        self.label_2.setStyleSheet(self.GREY_CARD_TILE)
        self.label_4.setStyleSheet(self.GREY_CARD_TILE)

    def __loadConfig(self, field: QtWidgets.QLineEdit, fileType):
        self.__clear_message()
        self.__setFilePath(field, fileType)
        self.config_File_name_readOnly.setText(self.config_File_name.text())
        if field.text() and (path.exists(field.text()) and os.path.getsize(field.text()) > 0):
            self.__setDefaultValues(field.text())

    def __clear_message(self):
        self.message.setText("")
        self.message.setStyleSheet(self.WHITE_BACKGROUND)

    def __setFilePath(self, field: QtWidgets.QLineEdit, fileType):
        directoryPath = Path(__file__).parents[2]
        path_to_file, _ = QFileDialog.getOpenFileName(None, "Load File Path", directoryPath.__str__(), fileType, None)
        field.setText(path_to_file)

    def __save(self):
        self.__clear_message()
        fileName = self.config_File_name.text()
        is_create_new_file = fileName is None or not fileName
        is_create_new_file = is_create_new_file or not path.exists(fileName)
        is_create_new_file = is_create_new_file or (path.exists(fileName) and os.path.getsize(fileName) == 0)

        if fileName is None or not fileName:
            parentPath = Path(__file__).parents[2]
            fileName = path.join(parentPath.__str__(), 'config.yml')

        if is_create_new_file:
            self.config_File_name.setText(fileName)
            config = self.__create_new_config(fileName)
        else:
            config = yaml.load(open(fileName))

        try:
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
            self.config_File_name_readOnly.setText(self.config_File_name.text())
            self.__set_message("  Configuration file updated.", self.SUCCESS_MESSAGE_STYLE)
        except TypeError:
            self.__set_message("  Error: Cannot update file. Invalid config file", self.ERROR_MESSAGE_STYLE)

    def __create_new_config(self, fileName):
        data = dict(
            configuration=dict(),
            umapi=dict()
        )
        yaml.dump(data, open(fileName, "w+"), default_flow_style=False)
        config = yaml.load(open(fileName))
        return config

    def __setDefaultValues(self, configFile):
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
            self.__set_message("  Error: Unable to load configuration. Invalid config file", self.ERROR_MESSAGE_STYLE)

    def __set_message(self, message_string, style):
        self.message.setText(message_string)
        self.message.setStyleSheet(style)

    def __run_user_update(self):
        command = 'python ../user_update.py -c ' +  self.config_File_name_readOnly.text()
        exit_code= os.system(command)
        return exit_code


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(590, 561)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.update_window_config()
    MainWindow.show()
    sys.exit(app.exec_())
