from PyQt5.QtCore import Qt
import os
from edit import *
from PyQt5.QtWidgets import (
    QLabel, QVBoxLayout,
    QLineEdit, QApplication, QPushButton, QHBoxLayout, QWidget, QListWidget , QFileDialog)
app = QApplication([])
win = QWidget()
btn_dir = QPushButton("Папка")
workdir = QFileDialog.getExistingDirectory()










win.setLayout(row)
