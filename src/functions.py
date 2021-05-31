import json

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

from resources import constants as c


def load_json(user_file):
    with open("{}/{}.json".format(c.BACKEND, user_file), 'rt') as f_in:
        data = json.load(f_in)
    return data


def dump_json(user_file, data):
    with open("{}/{}.json".format(c.BACKEND, user_file), 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


def prompt_user(action, text, title):
    msg_box = QMessageBox()
    msg_box.setWindowIcon(QtGui.QIcon(c.BRAIN))
    msg_box.setText(text)
    msg_box.setWindowTitle(title)

    if action == "?":
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    if action == "i":
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    if action == "!":
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    return msg_box.exec()

