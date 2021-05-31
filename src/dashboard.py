import os

from PyQt5 import QtWidgets, uic, QtGui
from resources import constants as c

from src import functions as f
from src import home


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        uic.loadUi(c.DASHBOARD, self)

        self.setup_ui()

    def setup_ui(self):

        self.setWindowIcon(QtGui.QIcon(c.BRAIN))
        self.lblName.setVisible(False)
        self.txtName.setVisible(False)
        self.lblNoAccount.setVisible(True)
        self.btnRegister.setGeometry(210, 20, 40, 16)
        self.btnRegister.setText("here")
        self.btnLogin.setText("Login")
        self.btnLogin.setGeometry(310, 320, 190, 61)

        self.btnLogin.clicked.connect(self.action)
        self.btnRegister.clicked.connect(self.register)

    def register(self):
        if self.btnRegister.text() == "here":
            self.btnLogin.setGeometry(310, 380, 190, 61)
            self.btnLogin.setText("Register")
            self.lblName.setVisible(True)
            self.txtName.setVisible(True)
            self.lblNoAccount.setVisible(False)
            self.btnRegister.setGeometry(10, 20, 40, 16)
            self.btnRegister.setText("home")
        elif self.btnRegister.text() == "home":
            self.setup_ui()

    def action(self):
        if self.btnLogin.text() == "Login":
            username = self.txtUsername.toPlainText()
            user_exists = False
            try:
                if username == "":
                    f.prompt_user("i", text="Please enter a username to continue...", title="Empty field")
                else:
                    for file in os.listdir(c.BACKEND):
                        if file[:-5] == username.lower():
                            user_exists = True
                            break
                        else:
                            user_exists = False
                    if user_exists:
                        data = f.load_json(username)
                        self.switch_home(data)
                    else:
                        f.prompt_user("i", text="Username not found in database.\n"
                                                "Please create account.", title="Not found")
                        self.txtUsername.clear()
            except Exception as e:
                f.prompt_user("!", text="Login error. Error code: {}".format(e), title="Error")
        elif self.btnLogin.text() == "Register":
            try:
                username = self.txtUsername.toPlainText()
                name = self.txtName.toPlainText()

                data = {
                    "USERNAME": username,
                    "NAME": name,
                    "MOVIES": [],
                    "EATS": []
                }
                f.dump_json(username, data)

                f.prompt_user("i", text="Account created successfully.", title="New Account")
                self.txtUsername.clear()
                self.txtName.clear()
                self.setup_ui()
            except Exception as e:
                f.prompt_user("!", text="Error creating new account.\n"
                                        "Error code: {}".format(e), title="Error")

    def switch_home(self, data):
        self.window = home.Home(data)
        self.window.show()
        self.close()
