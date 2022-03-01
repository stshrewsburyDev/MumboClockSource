import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from engine import themeUi


class Ui_Dialog(object):
    def __init__(self, dialog):
        # Setup translator
        self._translate = QtCore.QCoreApplication.translate

        # Window setup
        self.dialog = dialog
        self.dialog.setObjectName("Dialog")
        self.dialog.setEnabled(True)
        self.dialog.resize(521, 511)
        # Setup size policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog.sizePolicy().hasHeightForWidth())
        self.dialog.setSizePolicy(sizePolicy)
        self.dialog.setMinimumSize(QtCore.QSize(521, 511))
        self.dialog.setMaximumSize(QtCore.QSize(521, 511))
        self.dialog.setWindowTitle(self._translate("Dialog", "Mumbo clock - About"))

        # Setup icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("image", "icon", "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        # Setting up custom font(s)
        bebasFont = QtGui.QFont()
        bebasFont.setFamily("Bebas")
        bebasFont.setPointSize(40)

        # Main title
        # Icon
        self.title_icon = QtWidgets.QLabel(self.dialog)
        self.title_icon.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.title_icon.setText("")
        self.title_icon.setPixmap(QtGui.QPixmap("../MumboClock/image/icon/icon.png"))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")
        # Text
        self.title_label = QtWidgets.QLabel(self.dialog)
        self.title_label.setGeometry(QtCore.QRect(110, 10, 401, 91))
        self.title_label.setFont(bebasFont)
        self.title_label.setObjectName("title_label")
        self.title_label.setText(self._translate("Dialog", "About Mumbo clock:"))

        # Setup labels
        self.about01 = QtWidgets.QLabel(self.dialog)
        self.about01.setGeometry(QtCore.QRect(10, 110, 501, 21))
        self.about01.setObjectName("about01")
        self.about01.setText(self._translate("Dialog", "Name: Mumbo clock"))

        self.about02 = QtWidgets.QLabel(self.dialog)
        self.about02.setGeometry(QtCore.QRect(10, 130, 501, 21))
        self.about02.setObjectName("about02")
        self.about02.setText(self._translate("Dialog", "Version: 1.0"))

        self.about03 = QtWidgets.QLabel(self.dialog)
        self.about03.setGeometry(QtCore.QRect(10, 150, 501, 21))
        self.about03.setObjectName("about03")
        self.about03.setText(self._translate("Dialog", "Developed by: stshrewsburyDev (Steven Shrewsbury)"))

        self.about04 = QtWidgets.QLabel(self.dialog)
        self.about04.setGeometry(QtCore.QRect(10, 170, 501, 21))
        self.about04.setObjectName("about04")
        self.about04.setText(self._translate("Dialog", "Original clock creator: ElyBeatMaker"))

        self.about05 = QtWidgets.QLabel(self.dialog)
        self.about05.setGeometry(QtCore.QRect(10, 190, 501, 21))
        self.about05.setObjectName("about05")
        self.about05.setText(self._translate("Dialog", "Special thanks to:"))

        self.about06 = QtWidgets.QLabel(self.dialog)
        self.about06.setGeometry(QtCore.QRect(30, 210, 481, 21))
        self.about06.setObjectName("about06")
        self.about06.setText(self._translate("Dialog", "- ElyBeatMaker for the amazing idea of making a Mumbo Jumbo clock and providing assets"))

        self.about07 = QtWidgets.QLabel(self.dialog)
        self.about07.setGeometry(QtCore.QRect(30, 230, 481, 21))
        self.about07.setObjectName("about07")
        self.about07.setText(self._translate("Dialog", "- Enrico for doing stuff"))

        self.about08 = QtWidgets.QLabel(self.dialog)
        self.about08.setGeometry(QtCore.QRect(30, 250, 481, 21))
        self.about08.setObjectName("about08")
        self.about08.setText(self._translate("Dialog", "- NanoDano from DevDungeon for some help with windowing problems I had"))

        self.about09 = QtWidgets.QLabel(self.dialog)
        self.about09.setGeometry(QtCore.QRect(30, 270, 481, 21))
        self.about09.setObjectName("about09")
        self.about09.setText(self._translate("Dialog", "- College music for providing a amazing chill music stream that helped me stay focused and chill"))

        self.about10 = QtWidgets.QLabel(self.dialog)
        self.about10.setGeometry(QtCore.QRect(30, 290, 481, 21))
        self.about10.setObjectName("about10")
        self.about10.setText(self._translate("Dialog", "- Mumbo Jumbo for making the original inspiration for the outro time song and this clock"))

        self.about11 = QtWidgets.QLabel(self.dialog)
        self.about11.setGeometry(QtCore.QRect(30, 310, 481, 21))
        self.about11.setObjectName("about11")
        self.about11.setText(self._translate("Dialog", "- Everyone on twitter and Ely\'s discord server that supported the development of Mumbo clock"))

        self.links01 = QtWidgets.QLabel(self.dialog)
        self.links01.setGeometry(QtCore.QRect(10, 360, 501, 21))
        self.links01.setObjectName("links01")
        self.links01.setText(self._translate("Dialog", "<b><u>Check these out:</u></b>"))

        self.links02 = QtWidgets.QLabel(self.dialog)
        self.links02.setGeometry(QtCore.QRect(30, 380, 481, 21))
        self.links02.setObjectName("links02")
        self.links02.setText(self._translate("Dialog", "- <a href=\"http://elybeatmaker.com/mumboclock.html\">Online Mumbo clock by Enrico</a>"))
        self.links02.setOpenExternalLinks(True)

        self.links03 = QtWidgets.QLabel(self.dialog)
        self.links03.setGeometry(QtCore.QRect(30, 400, 481, 21))
        self.links03.setObjectName("links03")
        self.links03.setText(self._translate("Dialog", "- <a href=\"http://elybeatmaker.com\">ElyBeatMakers website</a>"))
        self.links03.setOpenExternalLinks(True)

        self.links04 = QtWidgets.QLabel(self.dialog)
        self.links04.setGeometry(QtCore.QRect(30, 420, 481, 21))
        self.links04.setObjectName("links04")
        self.links04.setText(self._translate("Dialog", "- <a href=\"https://www.youtube.com/elybeatmaker\">ElyBeatMakers YouTube</a>"))
        self.links04.setOpenExternalLinks(True)

        self.links05 = QtWidgets.QLabel(self.dialog)
        self.links05.setGeometry(QtCore.QRect(30, 440, 481, 21))
        self.links05.setObjectName("links05")
        self.links05.setText(self._translate("Dialog", "- <a href=\"https://github.com/stshrewsburyDev/Mumbo-clock\">Mumbo clock GitHub repository</a>"))
        self.links05.setOpenExternalLinks(True)

        # Setup buttons
        self.ok_button = QtWidgets.QPushButton(self.dialog)
        self.ok_button.setGeometry(QtCore.QRect(70, 470, 381, 31))
        self.ok_button.setObjectName("pushButton")
        self.ok_button.setText(self._translate("Dialog", "Close"))
        self.ok_button.clicked.connect(QtWidgets.qApp.quit)

        # Do whatever this does
        QtCore.QMetaObject.connectSlotsByName(self.dialog)


def open_window():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(themeUi.ui_theme)
    aboutUI = QtWidgets.QDialog()

    # Initialise custom font
    QtGui.QFontDatabase.addApplicationFont(os.path.join("font", "bebasRegular.ttf"))

    ui = Ui_Dialog(dialog=aboutUI)

    aboutUI.show()
    app.exec_()

    return


if __name__ == "__main__":
    open_window()
