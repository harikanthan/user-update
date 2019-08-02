from PySide2 import QtCore, QtGui, QtWidgets
from ui.ui_main_window_base import Ui_MainWindowBase
import config.config_loader as config_loader
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import QObject
import sys

class Ui_MainWindow(Ui_MainWindowBase):

    def updateWindowConfig(self):
        self.setDefaultValues()
        self.save.clicked.connect(self.__save)
        self.privateKeyPath.clicked.connect(lambda:self.__setFilePath(self.private_key_file))
        self.userListFilePath.clicked.connect(lambda:self.__setFilePath(self.users_filename))

    def __setFilePath(self, field: QtWidgets.QLineEdit):
        path_to_file, _ = QFileDialog.getOpenFileName(None,"Load File Path",None,"*.*",None)
        field.setText(path_to_file)

    def __save(self):
        print(self.id_type.text())

    def setDefaultValues(self):
        umapi, config = config_loader.ConfigLoader().load_config(config_filename="../example-config.yml")
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


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(674, 550)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.updateWindowConfig()

    MainWindow.show()
    sys.exit(app.exec_())
