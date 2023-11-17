import os.path
import sys
import subprocess

from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QLabel
from PySide6 import QtCore
from UserInterfacesPandora import qdarkstyle
import Pandora_Maya_Integration
class PandoraInstallerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UIW Pandora Auto Installer 0.0.1")

        #Widgets
        self.maya_path_hint = QLabel("Maya Document Path should be C:\\Users\\your_user_name\\Documents\\maya\\maya_version")
        self.maya_path_label = QLabel("Maya Document Path: ")
        self.maya_path_field = QLineEdit()
        self.load_path_button = QPushButton("...")
        self.install_button = QPushButton("Install")

        #layout
        self.layout = QVBoxLayout(self)
        self.path_layout = QHBoxLayout(self)

        self.layout.addWidget(self.maya_path_hint)

        self.layout.addLayout(self.path_layout)
        self.path_layout.addWidget(self.maya_path_label)
        self.path_layout.addWidget(self.maya_path_field)
        self.path_layout.addWidget(self.load_path_button)

        self.layout.addWidget(self.install_button)


        #deault values:
        documents_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        self.maya_path_field.setText(documents_path + "/maya/2024")

        #functionality
        self.load_path_button.clicked.connect(self.pick_maya_path)
        self.install_button.clicked.connect(self.install)


        #style
        self.resize(600, 100)
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))



    def pick_maya_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog

        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)

        if directory:
            self.maya_path_field.setText(directory)

    def install(self):
        exec_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(os.path.abspath(exec_dir))
        os.chdir(parent_dir)
        vendor_installer_name = "Pandora_Setup.bat"
        vendor_installer_path = os.path.join(parent_dir, vendor_installer_name)
        print(vendor_installer_path)
        subprocess.run([vendor_installer_path])

if __name__ == "__main__":
    app = QApplication([])
    widget = PandoraInstallerWidget()
    widget.show()

    sys.exit(app.exec())