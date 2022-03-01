import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from engine import themeUi
from engine import themeThumbnailMaker
from engine import themeManager
from engine import settingsManager
from engine import settingsConfiguration


class Ui_Dialog(object):
    def __init__(self, dialog):
        # Setup lines theme
        self.lineTheme = QtGui.QPalette()
        self.lineTheme.setColor(QtGui.QPalette.WindowText, QtGui.QColor(80, 80, 80))

        # Setup settings
        self.settings = settingsManager.Settings()
        self.currentSettings = self.settings.get_settings()
        self.defaultSettings = settingsConfiguration.SettingsConfiguration(self.settings.defaultSettings)

        # Setup themes
        self.themes = themeManager.ThemeManager()
        self.themeList = self.themes.get_all_themes_list()

        self.themeNameList = []

        # Setup translator
        self._translate = QtCore.QCoreApplication.translate

        # Setup update timer
        self.updateTimer = QtCore.QTimer()
        self.updateTimer.setInterval(50)
        self.updateTimer.timeout.connect(self.update_ui)

        # Window setup
        self.dialog = dialog
        self.dialog.setObjectName("Dialog")
        self.dialog.setEnabled(True)
        self.dialog.resize(971, 591)
        # Setup size policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog.sizePolicy().hasHeightForWidth())
        self.dialog.setSizePolicy(sizePolicy)
        self.dialog.setMinimumSize(QtCore.QSize(971, 591))
        self.dialog.setMaximumSize(QtCore.QSize(971, 591))
        self.dialog.setWindowTitle(self._translate("Dialog", "Mumbo clock - Configuration settings"))

        # Setup icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("image", "icon", "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        # Setting up custom font(s)
        bebasFont = QtGui.QFont()
        bebasFont.setFamily("Bebas")
        bebasFont.setPointSize(35)

        # Main title
        # Icon
        self.title_icon = QtWidgets.QLabel(self.dialog)
        self.title_icon.setGeometry(QtCore.QRect(190, 10, 81, 81))
        self.title_icon.setText("")
        self.title_icon.setPixmap(QtGui.QPixmap(os.path.join("image", "icon", "icon.png")))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")
        # Text
        self.title_text = QtWidgets.QLabel(self.dialog)
        self.title_text.setGeometry(QtCore.QRect(276, 10, 481, 81))
        self.title_text.setFont(bebasFont)
        self.title_text.setObjectName("title_text")
        self.title_text.setText(self._translate("Dialog", "Mumbo clock configuration"))

        # Setup lines
        self.divider_1 = QtWidgets.QFrame(self.dialog)
        self.divider_1.setGeometry(QtCore.QRect(10, 200, 951, 21))
        self.divider_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_1.setLineWidth(2)
        self.divider_1.setPalette(self.lineTheme)
        self.divider_1.setObjectName("divider_1")

        self.divider_2 = QtWidgets.QFrame(self.dialog)
        self.divider_2.setGeometry(QtCore.QRect(10, 410, 951, 21))
        self.divider_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_2.setLineWidth(2)
        self.divider_2.setPalette(self.lineTheme)
        self.divider_2.setObjectName("divider_2")

        self.divider_3 = QtWidgets.QFrame(self.dialog)
        self.divider_3.setGeometry(QtCore.QRect(10, 510, 951, 21))
        self.divider_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_3.setLineWidth(2)
        self.divider_3.setPalette(self.lineTheme)
        self.divider_3.setObjectName("divider_3")

        self.vertical_1 = QtWidgets.QFrame(self.dialog)
        self.vertical_1.setGeometry(QtCore.QRect(500, 340, 21, 61))
        self.vertical_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_1.setLineWidth(1)
        self.vertical_1.setPalette(self.lineTheme)
        self.vertical_1.setObjectName("vertical_1")

        # Setup labels
        self.label_win_size = QtWidgets.QLabel(self.dialog)
        self.label_win_size.setGeometry(QtCore.QRect(490, 110, 101, 21))
        self.label_win_size.setObjectName("label_win_size")
        self.label_win_size.setText(self._translate("Dialog", "Clock size (pixels):"))

        self.label_fps_limit = QtWidgets.QLabel(self.dialog)
        self.label_fps_limit.setGeometry(QtCore.QRect(490, 140, 101, 21))
        self.label_fps_limit.setObjectName("label_fps_limit")
        self.label_fps_limit.setText(self._translate("Dialog", "FPS limit:"))

        self.label_theme = QtWidgets.QLabel(self.dialog)
        self.label_theme.setGeometry(QtCore.QRect(179, 430, 41, 71))
        self.label_theme.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theme.setObjectName("label_theme")
        self.label_theme.setText(self._translate("Dialog", "Theme:"))

        self.label_seasonal_modes = QtWidgets.QLabel(self.dialog)
        self.label_seasonal_modes.setGeometry(QtCore.QRect(491, 320, 471, 21))
        self.label_seasonal_modes.setObjectName("label_seasonal_modes")
        self.label_seasonal_modes.setText(self._translate("Dialog", "Seasonal modes (works with \"grian mode\" or \"No moustache mode\"):"))

        # Setup preview labels
        self.preview_clock_size = QtWidgets.QLabel(self.dialog)
        self.preview_clock_size.setGeometry(QtCore.QRect(910, 110, 51, 21))
        self.preview_clock_size.setObjectName("preview_clock_size")

        self.preview_fps_limit = QtWidgets.QLabel(self.dialog)
        self.preview_fps_limit.setGeometry(QtCore.QRect(910, 140, 51, 21))
        self.preview_fps_limit.setObjectName("preview_fps_limit")

        # Setup check boxs
        self.check_box_show_fps = QtWidgets.QCheckBox(self.dialog)
        self.check_box_show_fps.setGeometry(QtCore.QRect(10, 110, 471, 21))
        self.check_box_show_fps.setObjectName("check_box_show_fps")
        self.check_box_show_fps.setText(self._translate("Dialog", "Show FPS (frames per second)"))

        self.check_box_borderless_win = QtWidgets.QCheckBox(self.dialog)
        self.check_box_borderless_win.setGeometry(QtCore.QRect(10, 140, 471, 21))
        self.check_box_borderless_win.setObjectName("check_box_borderless_win")
        self.check_box_borderless_win.setText(self._translate("Dialog", "Borderless window mode (removes title bar and lines from around clock window)"))

        self.check_box_chroma_key = QtWidgets.QCheckBox(self.dialog)
        self.check_box_chroma_key.setGeometry(QtCore.QRect(10, 170, 471, 21))
        self.check_box_chroma_key.setObjectName("check_box_chroma_key")
        self.check_box_chroma_key.setText(self._translate("Dialog", "Enable chroma key (allows the window to be transparent)"))

        # Setup sliders (Put this here as a simple fix for the TAB ordering)
        # Win size
        self.slider_win_size = QtWidgets.QSlider(self.dialog)
        self.slider_win_size.setGeometry(QtCore.QRect(600, 111, 301, 21))
        self.slider_win_size.setMinimum(100)
        self.slider_win_size.setMaximum(750)
        self.slider_win_size.setSingleStep(5)
        self.slider_win_size.setPageStep(5)
        self.slider_win_size.setOrientation(QtCore.Qt.Horizontal)
        self.slider_win_size.setObjectName("slider_win_size")
        # FPS limit
        self.slider_fps_limit = QtWidgets.QSlider(self.dialog)
        self.slider_fps_limit.setGeometry(QtCore.QRect(600, 140, 301, 21))
        self.slider_fps_limit.setMinimum(5)
        self.slider_fps_limit.setMaximum(60)
        self.slider_fps_limit.setSingleStep(5)
        self.slider_fps_limit.setPageStep(5)
        self.slider_fps_limit.setOrientation(QtCore.Qt.Horizontal)
        self.slider_fps_limit.setObjectName("slider_fps_limit")

        # Back to setup of check boxs
        self.check_box_animations = QtWidgets.QCheckBox(self.dialog)
        self.check_box_animations.setGeometry(QtCore.QRect(10, 230, 471, 21))
        self.check_box_animations.setObjectName("check_box_animations")
        self.check_box_animations.setText(self._translate("Dialog", "Show clock animations (may improve framerate)"))

        self.check_box_clock_numbers = QtWidgets.QCheckBox(self.dialog)
        self.check_box_clock_numbers.setGeometry(QtCore.QRect(10, 260, 471, 21))
        self.check_box_clock_numbers.setObjectName("check_box_clock_numbers")
        self.check_box_clock_numbers.setText(self._translate("Dialog", "Show clock face numbers"))

        self.check_box_clock_border = QtWidgets.QCheckBox(self.dialog)
        self.check_box_clock_border.setGeometry(QtCore.QRect(10, 290, 471, 21))
        self.check_box_clock_border.setObjectName("check_box_clock_border")
        self.check_box_clock_border.setText(self._translate("Dialog", "Show clock face border"))

        self.check_box_clock_hour_lines = QtWidgets.QCheckBox(self.dialog)
        self.check_box_clock_hour_lines.setGeometry(QtCore.QRect(10, 320, 471, 21))
        self.check_box_clock_hour_lines.setObjectName("check_box_clock_hour_lines")
        self.check_box_clock_hour_lines.setText(self._translate("Dialog", "Show clock face hour lines"))

        self.check_box_clock_min_lines = QtWidgets.QCheckBox(self.dialog)
        self.check_box_clock_min_lines.setGeometry(QtCore.QRect(10, 350, 471, 21))
        self.check_box_clock_min_lines.setObjectName("check_box_clock_min_lines")
        self.check_box_clock_min_lines.setText(self._translate("Dialog", "Show clock face minute lines (disabled if \"show clock face hour lines\" is disabled)"))

        self.check_box_night_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_night_mode.setGeometry(QtCore.QRect(10, 380, 471, 21))
        self.check_box_night_mode.setObjectName("check_box_night_mode")
        self.check_box_night_mode.setText(self._translate("Dialog", "Enable night hours (visible from 10PM to 8AM)"))

        self.check_box_spoon_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_spoon_mode.setGeometry(QtCore.QRect(490, 230, 471, 21))
        self.check_box_spoon_mode.setObjectName("check_box_spoon_mode")
        self.check_box_spoon_mode.setText(self._translate("Dialog", "Enable spoon hours (visible from 12PM to 2PM)"))

        self.check_box_moustache_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_moustache_mode.setGeometry(QtCore.QRect(490, 260, 471, 21))
        self.check_box_moustache_mode.setObjectName("check_box_moustache_mode")
        self.check_box_moustache_mode.setText(self._translate("Dialog", "No moustache mode (disabled if \"grian mode\" enabled)"))

        self.check_box_grian_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_grian_mode.setGeometry(QtCore.QRect(490, 290, 471, 21))
        self.check_box_grian_mode.setObjectName("check_box_grian_mode")
        self.check_box_grian_mode.setText(self._translate("Dialog", "Grian mode"))

        self.check_box_xmas_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_xmas_mode.setGeometry(QtCore.QRect(521, 350, 441, 21))
        self.check_box_xmas_mode.setObjectName("check_box_xmas_mode")
        self.check_box_xmas_mode.setText(self._translate("Dialog", "Christmas mode (visible from 1st December to 25th December)"))

        self.check_box_bday_mode = QtWidgets.QCheckBox(self.dialog)
        self.check_box_bday_mode.setGeometry(QtCore.QRect(521, 380, 441, 21))
        self.check_box_bday_mode.setObjectName("check_box_bday_mode")
        self.check_box_bday_mode.setText(self._translate("Dialog", "Birthday mode (visible on Mumbos birthday (1st December))"))

        # Setup combo box
        self.combo_box_theme = QtWidgets.QComboBox(self.dialog)
        self.combo_box_theme.setGeometry(QtCore.QRect(229, 430, 541, 71))
        self.combo_box_theme.setIconSize(QtCore.QSize(64, 64))
        self.combo_box_theme.setObjectName("combo_box_theme")
        self.setup_combobox()

        # Setup buttons
        # Reset
        self.button_reset_defaults = QtWidgets.QPushButton(self.dialog)
        self.button_reset_defaults.setGeometry(QtCore.QRect(240, 540, 131, 31))
        self.button_reset_defaults.setObjectName("button_reset_defaults")
        self.button_reset_defaults.setText(self._translate("Dialog", "Reset to defaults"))
        self.button_reset_defaults.clicked.connect(lambda:self.set_ui_current_settings(self.defaultSettings))
        # Save
        self.button_save = QtWidgets.QPushButton(self.dialog)
        self.button_save.setGeometry(QtCore.QRect(420, 540, 131, 31))
        self.button_save.setObjectName("button_save")
        self.button_save.setText(self._translate("Dialog", "Save settings"))
        self.button_save.clicked.connect(self.save_and_exit)
        # Close
        self.button_close = QtWidgets.QPushButton(self.dialog)
        self.button_close.setGeometry(QtCore.QRect(600, 540, 131, 31))
        self.button_close.setObjectName("button_close")
        self.button_close.setText(self._translate("Dialog", "Close"))
        self.button_close.clicked.connect(QtWidgets.qApp.quit)

        # Set UI to show current settings
        self.set_ui_current_settings(settings=self.currentSettings)

        # Start UI updates
        self.updateTimer.start()

        # Do whatever this does
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    @staticmethod
    def bool_to_bin(booleanExpression):
        if booleanExpression:
            return 1
        return 0

    def setup_combobox(self):
        x = 0

        for theme in self.themeList:
            self.themeNameList.append(theme.name.lower())
            icon = QtGui.QIcon()
            iconRenderPath = os.path.join("image", "themeIcons", "{}".format(theme.thumbnail))
            if not os.path.isfile(iconRenderPath):
                try:
                    themeThumbnailMaker.draw_icon(theme=theme, PATH=iconRenderPath)
                    icon.addPixmap(QtGui.QPixmap(iconRenderPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                except Exception as error:
                    print("Exception in engine.configurationWindow.Ui_dialog.setup_combobox(): {}".format(error))
                    icon.addPixmap(QtGui.QPixmap(os.path.join("image", "icon", "icon512x.png")), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            else:
                icon.addPixmap(QtGui.QPixmap(iconRenderPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            name = "{0.name} by {0.creator}".format(theme)
            self.combo_box_theme.addItem(icon, name)

            x += 1

    def update_ui(self):
        self.preview_clock_size.setText(self._translate("Dialog", "{} px".format(self.slider_win_size.value())))
        self.preview_fps_limit.setText(self._translate("Dialog", "{} FPS".format(self.slider_fps_limit.value())))

        if not self.check_box_clock_hour_lines.isChecked():
            self.check_box_clock_min_lines.setChecked(False)
            self.check_box_clock_min_lines.setDisabled(True)
        else:
            self.check_box_clock_min_lines.setDisabled(False)

        if self.check_box_grian_mode.isChecked():
            self.check_box_moustache_mode.setChecked(False)
            self.check_box_moustache_mode.setDisabled(True)
        else:
            self.check_box_moustache_mode.setDisabled(False)

    def set_ui_current_settings(self, settings: settingsConfiguration.SettingsConfiguration):
        self.slider_win_size.setValue(settings.winSize)
        self.slider_fps_limit.setValue(settings.FPSLimit)

        self.check_box_show_fps.setChecked(settings.showFPS)
        self.check_box_borderless_win.setChecked(settings.borderlessWin)
        self.check_box_chroma_key.setChecked(settings.enableChroma)

        self.check_box_animations.setChecked(settings.showAnimations)
        self.check_box_clock_numbers.setChecked(settings.showNumbers)
        self.check_box_clock_border.setChecked(settings.showBorder)
        self.check_box_clock_hour_lines.setChecked(settings.showHourLines)
        self.check_box_clock_min_lines.setChecked(settings.showMinLines)
        self.check_box_night_mode.setChecked(settings.nightModeActive)
        self.check_box_spoon_mode.setChecked(settings.spoonHoursActive)
        self.check_box_moustache_mode.setChecked(settings.noMustacheMode)
        self.check_box_grian_mode.setChecked(settings.grianMode)
        self.check_box_xmas_mode.setChecked(settings.xmasMode)
        self.check_box_bday_mode.setChecked(settings.birthdayMode)

        self.combo_box_theme.setCurrentIndex(self.themeNameList.index(settings.theme.lower()))

    def save_and_exit(self):
        current_theme = self.themeList[self.combo_box_theme.currentIndex()]
        compiled_settings = {"winSize": self.slider_win_size.value(),
                             "showFPS": self.bool_to_bin(self.check_box_show_fps.isChecked()),
                             "FPSLimit": self.slider_fps_limit.value(),
                             "borderlessWin": self.bool_to_bin(self.check_box_borderless_win.isChecked()),
                             "enableChroma": self.bool_to_bin(self.check_box_chroma_key.isChecked()),
                             "theme": current_theme.name,
                             "showAnimations": self.bool_to_bin(self.check_box_animations.isChecked()),
                             "showNumbers": self.bool_to_bin(self.check_box_clock_numbers.isChecked()),
                             "showHourLines": self.bool_to_bin(self.check_box_clock_hour_lines.isChecked()),
                             "showMinLines": self.bool_to_bin(self.check_box_clock_min_lines.isChecked()),
                             "showBorder": self.bool_to_bin(self.check_box_clock_border.isChecked()),
                             "nightModeActive": self.bool_to_bin(self.check_box_night_mode.isChecked()),
                             "spoonHoursModeActive": self.bool_to_bin(self.check_box_spoon_mode.isChecked()),
                             "noMustacheMode": self.bool_to_bin(self.check_box_moustache_mode.isChecked()),
                             "grianMode": self.bool_to_bin(self.check_box_grian_mode.isChecked()),
                             "seasonalModes": {
                                 "birthday": self.bool_to_bin(self.check_box_bday_mode.isChecked()),
                                 "xmas": self.bool_to_bin(self.check_box_xmas_mode.isChecked())
                             }}

        self.settings.save_settings(settings=compiled_settings)
        self.openRestartRequiredWin = True
        QtWidgets.QMessageBox.about(self.dialog, "Restart required", "To apply your new settings, the clock must be restarted.")
        self.dialog.close()


def open_window():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(themeUi.ui_theme)
    configUI = QtWidgets.QDialog()

    # Initialise custom font:
    QtGui.QFontDatabase.addApplicationFont(os.path.join("font", "bebasRegular.ttf"))

    ui = Ui_Dialog(dialog=configUI)

    configUI.show()
    app.exec_()

    return


if __name__ == "__main__":
    open_window()
