from random import randrange

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox

from resources import constants as c

from src import functions as f
from src import dashboard as db


class Home(QtWidgets.QMainWindow):
    def __init__(self, user_data):
        super(Home, self).__init__()
        uic.loadUi(c.HOME, self)

        self.user_data = user_data
        self.lblName.setText(self.user_data["NAME"])

        self.slider.valueChanged.connect(self.slider_action)
        self.btnLogOut.clicked.connect(self.switch_home)
        self.btnMovies.clicked.connect(lambda: self.action(value="movie"))
        self.btnEats.clicked.connect(lambda: self.action(value="eats"))
        self.btnHome.clicked.connect(self.setup_ui)
        self.btnMovieList.clicked.connect(lambda: self.action(value="movie_list"))
        self.btnFoodList.clicked.connect(lambda: self.action(value="food_list"))
        self.btnAdd.clicked.connect(self.add)
        self.btnPick.clicked.connect(self.get_item)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon(c.BRAIN))
        self.btnColor.setIcon(QtGui.QIcon(c.COLOR))
        self.btnLogOut.setIcon(QtGui.QIcon(c.LOGOUT))
        self.btnDelete.setIcon(QtGui.QIcon(c.DELETE))
        self.btnMovieList.setIcon(QtGui.QIcon(c.MOVIE))
        self.btnFoodList.setIcon(QtGui.QIcon(c.FOOD))

        self.btnColor.setEnabled(False)
        self.btnRandomNumbers.setEnabled(False)

        self.lstDisplay.clear()

        self.lblDisplay.setVisible(True)
        self.lblAddMovie.setVisible(True)
        self.lblAddEats.setEnabled(True)
        self.lblAddEats.setVisible(True)
        self.txtEats.setEnabled(True)
        self.txtMovie.setVisible(True)
        self.txtEats.setVisible(True)
        self.slider.setVisible(True)
        self.slider.setValue(0)
        self.btnAdd.setVisible(True)
        self.btnEats.setEnabled(True)
        self.btnMovies.setEnabled(True)
        self.lblPick.setVisible(False)
        self.btnPick.setVisible(False)
        self.lblAddMovie.setEnabled(False)
        self.txtMovie.setEnabled(False)
        self.btnHome.setVisible(False)
        self.lstDisplay.setVisible(False)
        self.btnDelete.setVisible(False)

        self.lblDisplay.setText("ScatterBrained\nSolving Your Decisions For You")

    def slider_action(self):
        if self.slider.value() == 0:
            self.lblAddMovie.setEnabled(False)
            self.txtMovie.setEnabled(False)
            self.lblAddEats.setEnabled(True)
            self.txtEats.setEnabled(True)
        elif self.slider.value() == 1:
            self.lblAddEats.setEnabled(False)
            self.txtEats.setEnabled(False)
            self.lblAddMovie.setEnabled(True)
            self.txtMovie.setEnabled(True)

    def switch_home(self):
        answer = f.prompt_user("?", text="Are you sure you would like to log out.", title="Logout")
        if answer == QMessageBox.Yes:
            self.window = db.Dashboard()
            self.window.show()
            self.close()
        else:
            return

    def action(self, value):
        if value == "movie":
            self.lblPick.setText("What am I watching...")
            self.toggle_button_states()
            self.btnMovies.setEnabled(False)
            self.btnEats.setEnabled(True)
        elif value == "eats":
            self.lblPick.setText("Where am I eating...")
            self.toggle_button_states()
            self.btnEats.setEnabled(False)
            self.btnMovies.setEnabled(True)
        elif value == "movie_list":
            try:
                self.toggle_button_states_lists()
                self.lblAddMovie.setEnabled(True)
                self.txtMovie.setEnabled(True)
                self.lblAddEats.setEnabled(False)
                self.txtEats.setEnabled(False)
                self.slider.setValue(1)
                for movie in self.user_data["MOVIES"]:
                    self.lstDisplay.addItem(movie)
            except Exception as e:
                print(str(e))
        elif value == "food_list":
            try:
                self.toggle_button_states_lists()
                self.lblAddMovie.setEnabled(False)
                self.txtMovie.setEnabled(False)
                self.lblAddEats.setEnabled(True)
                self.txtEats.setEnabled(True)
                self.slider.setValue(0)
                for movie in self.user_data["EATS"]:
                    self.lstDisplay.addItem(movie)
            except Exception as e:
                print(str(e))

    def toggle_button_states(self):
        self.lblPick.setVisible(True)
        self.btnPick.setVisible(True)
        self.btnHome.setVisible(True)
        self.lblDisplay.setVisible(False)
        self.lstDisplay.setVisible(False)
        self.btnDelete.setVisible(False)
        self.lblAddMovie.setVisible(False)
        self.txtMovie.setVisible(False)
        self.lblAddEats.setVisible(False)
        self.txtEats.setVisible(False)
        self.slider.setVisible(False)
        self.btnAdd.setVisible(False)

    def toggle_button_states_lists(self):
        self.setup_ui()
        self.lblDisplay.setVisible(False)
        self.lstDisplay.setVisible(True)
        self.btnDelete.setVisible(True)
        self.btnHome.setVisible(True)

    def add(self):
        try:
            movie_title = self.txtMovie.toPlainText()
            eats_title = self.txtEats.toPlainText()
            if self.slider.value() == 1 and movie_title != "":
                self.user_data["MOVIES"].append(movie_title)
                self.user_data["MOVIES"].sort()
                data = self.user_data
                f.dump_json(self.user_data["USERNAME"], data)
                f.prompt_user("i", text="Added new movie to collection.", title="Added Movie")
                self.txtMovie.clear()
                self.lstDisplay.clear()
                for movie in self.user_data["MOVIES"]:
                    self.lstDisplay.addItem(movie)
            elif self.slider.value() == 1 and movie_title == "":
                f.prompt_user("i", text="Please enter a movie to continue...", title="Empty field")
            elif self.slider.value() == 0 and eats_title == "":
                f.prompt_user("i", text="Please enter a restaurant to continue...", title="Empty field")
            elif self.slider.value() == 0 and eats_title != "":
                self.user_data["EATS"].append(eats_title)
                data = self.user_data
                f.dump_json(self.user_data["USERNAME"], data)
                f.prompt_user("i", text="Added new restaurant to list.", title="Added Restaurant")
                self.txtEats.clear()
                self.setup_ui()
        except Exception as e:
            print(str(e))

    def get_item(self):
        if self.lblPick.text() == "What am I watching...":
            random_index = randrange(len(self.user_data["MOVIES"]))
            self.lblDisplay.setVisible(True)
            self.lblDisplay.setText(self.user_data["MOVIES"][random_index])
        elif self.lblPick.text() == "Where am I eating...":
            random_index = randrange(len(self.user_data["EATS"]))
            self.lblDisplay.setVisible(True)
            self.lblDisplay.setText(self.user_data["EATS"][random_index])
