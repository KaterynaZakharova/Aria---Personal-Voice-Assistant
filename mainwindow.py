from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 550)
        MainWindow.setMinimumSize(QtCore.QSize(780, 550))
        MainWindow.setMaximumSize(QtCore.QSize(780, 550))
        MainWindow.setStyleSheet("background-color: rgb(244, 244, 244);\n"
                                 "gridline-color: rgb(0, 0, 0);\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Chat = QtWidgets.QTextEdit(self.centralwidget)
        self.Chat.setGeometry(QtCore.QRect(30, 40, 450, 400))
        self.Chat.setMinimumSize(QtCore.QSize(450, 400))
        self.Chat.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Chat.setFont(font)
        self.Chat.setStyleSheet("background-color: white;\n"
                                "gridline-color: rgb(0, 0, 0);\n"
                                "border-radius: 20%;\n"
                                "border-style: solid;\n"
                                "border-width: 1px;\n"
                                "border-color: black;")
        self.Chat.setObjectName("Chat")
        self.Aria = QtWidgets.QLabel(self.centralwidget)
        self.Aria.setGeometry(QtCore.QRect(100, 10, 311, 21))
        self.Aria.setStyleSheet("border-style: none;")
        self.Aria.setObjectName("Aria")
        self.FAQ = QtWidgets.QLabel(self.centralwidget)
        self.FAQ.setGeometry(QtCore.QRect(500, 10, 261, 21))
        self.FAQ.setStyleSheet("border-style: none;")
        self.FAQ.setObjectName("FAQ")
        self.Microphone = QtWidgets.QPushButton(self.centralwidget)
        self.Microphone.setEnabled(True)
        self.Microphone.setGeometry(QtCore.QRect(210, 490, 71, 51))
        self.Microphone.setStyleSheet("background-color: white;\n"
                                      "gridline-color: rgb(0, 0, 0);\n"
                                      "border-radius: 25%;\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color: black;")
        self.Microphone.setIcon(QtGui.QIcon('Microphone_button.png'))
        self.Microphone.setIconSize(QtCore.QSize(100, 100))
        self.Microphone.setObjectName("Microphone")
        self.Text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_input.setGeometry(QtCore.QRect(30, 450, 391, 31))
        self.Text_input.setStyleSheet("background-color: white;\n"
                                      "gridline-color: rgb(0, 0, 0);\n"
                                      "border-radius: 10%;\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color: black;")
        self.Text_input.setText("")
        self.Text_input.setObjectName("Text_input")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(430, 450, 51, 31))
        self.Enter.setStyleSheet("background-color: white;\n"
                                 "gridline-color: rgb(0, 0, 0);\n"
                                 "border-radius: 10%;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: black;")
        self.Enter.setIcon(QtGui.QIcon('Enter_button.png'))
        self.Enter.setIconSize(QtCore.QSize(20, 20))
        self.Enter.setObjectName("Enter")
        self.Make_a_note_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Make_a_note_btn.setEnabled(True)
        self.Make_a_note_btn.setGeometry(QtCore.QRect(500, 40, 261, 31))
        self.Make_a_note_btn.setStyleSheet("background-color: white;\n"
                                           "gridline-color: rgb(0, 0, 0);\n"
                                           "border-radius: 15%;\n"
                                           "border-style: solid;\n"
                                           "border-width: 1px;\n"
                                           "color: black;\n"
                                           'font: 14pt Calibri;\n'
                                           "border-color: black;")
        self.Make_a_note_btn.setObjectName("Make_a_note_btn")
        self.Check_notes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Check_notes_btn.setEnabled(True)
        self.Check_notes_btn.setGeometry(QtCore.QRect(500, 80, 261, 31))
        self.Check_notes_btn.setStyleSheet("background-color: white;\n"
                                           "gridline-color: rgb(0, 0, 0);\n"
                                           "border-radius: 15%;\n"
                                           "border-style: solid;\n"
                                           "border-width: 1px;\n"
                                           "color: black;\n"
                                           'font: 14pt Calibri;\n'
                                           "border-color: black;")
        self.Check_notes_btn.setObjectName("Check_notes_btn")
        self.Open_MS_Word_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Open_MS_Word_btn.setEnabled(True)
        self.Open_MS_Word_btn.setGeometry(QtCore.QRect(500, 120, 261, 31))
        self.Open_MS_Word_btn.setStyleSheet("background-color: white;\n"
                                            "gridline-color: rgb(0, 0, 0);\n"
                                            "border-radius: 15%;\n"
                                            "border-style: solid;\n"
                                            "border-width: 1px;\n"
                                            "color: black;\n"
                                            'font: 14pt Calibri;\n'
                                            "border-color: black;")
        self.Open_MS_Word_btn.setObjectName("Open_MS_Word_btn")
        self.Show_random_picture_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Show_random_picture_btn.setEnabled(True)
        self.Show_random_picture_btn.setGeometry(QtCore.QRect(500, 160, 261, 31))
        self.Show_random_picture_btn.setStyleSheet("background-color: white;\n"
                                                   "gridline-color: rgb(0, 0, 0);\n"
                                                   "border-radius: 15%;\n"
                                                   "border-style: solid;\n"
                                                   "border-width: 1px;\n"
                                                   "color: black;\n"
                                                   'font: 14pt Calibri;\n'
                                                   "border-color: black;")
        self.Show_random_picture_btn.setObjectName("Show_random_picture_btn")
        self.Open_donnu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Open_donnu_btn.setEnabled(True)
        self.Open_donnu_btn.setGeometry(QtCore.QRect(500, 200, 261, 31))
        self.Open_donnu_btn.setStyleSheet("background-color: white;\n"
                                          "gridline-color: rgb(0, 0, 0);\n"
                                          "border-radius: 15%;\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "color: black;\n"
                                          'font: 14pt Calibri;\n'
                                          "border-color: black;")
        self.Open_donnu_btn.setObjectName("Open_donnu_btn")
        self.Play_music_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Play_music_btn.setEnabled(True)
        self.Play_music_btn.setGeometry(QtCore.QRect(500, 240, 261, 31))
        self.Play_music_btn.setStyleSheet("background-color: white;\n"
                                          "gridline-color: rgb(0, 0, 0);\n"
                                          "border-radius: 15%;\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "color: black;\n"
                                          'font: 14pt Calibri;\n'
                                          "border-color: black;")
        self.Play_music_btn.setObjectName("Play_music_btn")
        self.Play_video_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Play_video_btn.setEnabled(True)
        self.Play_video_btn.setGeometry(QtCore.QRect(500, 280, 261, 31))
        self.Play_video_btn.setStyleSheet("background-color: white;\n"
                                          "gridline-color: rgb(0, 0, 0);\n"
                                          "border-radius: 15%;\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "color: black;\n"
                                          'font: 14pt Calibri;\n'
                                          "border-color: black;")
        self.Play_video_btn.setObjectName("Play_video_btn")
        self.Play_DL_WT_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Play_DL_WT_btn.setEnabled(True)
        self.Play_DL_WT_btn.setGeometry(QtCore.QRect(500, 320, 261, 31))
        self.Play_DL_WT_btn.setStyleSheet("background-color: white;\n"
                                          "gridline-color: rgb(0, 0, 0);\n"
                                          "border-radius: 15%;\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "color: black;\n"
                                          'font: 14pt Calibri;\n'
                                          "border-color: black;")
        self.Play_DL_WT_btn.setObjectName("Play_DL_WT_btn")
        self.Show_random_number_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Show_random_number_btn.setEnabled(True)
        self.Show_random_number_btn.setGeometry(QtCore.QRect(500, 360, 261, 31))
        self.Show_random_number_btn.setStyleSheet("background-color: white;\n"
                                                  "gridline-color: rgb(0, 0, 0);\n"
                                                  "border-radius: 15%;\n"
                                                  "border-style: solid;\n"
                                                  "border-width: 1px;\n"
                                                  "color: black;\n"
                                                  'font: 14pt Calibri;\n'
                                                  "border-color: black;")
        self.Show_random_number_btn.setObjectName("Show_random_number_btn")
        self.Calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate_btn.setEnabled(True)
        self.Calculate_btn.setGeometry(QtCore.QRect(500, 400, 261, 31))
        self.Calculate_btn.setStyleSheet("background-color: white;\n"
                                         "gridline-color: rgb(0, 0, 0);\n"
                                         "border-radius: 15%;\n"
                                         "border-style: solid;\n"
                                         "border-width: 1px;\n"
                                         "color: black;\n"
                                         'font: 14pt Calibri;\n'
                                         "border-color: black;")
        self.Calculate_btn.setObjectName("Calculate_btn")
        self.Python_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Python_btn.setEnabled(True)
        self.Python_btn.setGeometry(QtCore.QRect(500, 440, 261, 31))
        self.Python_btn.setStyleSheet("background-color: white;\n"
                                      "gridline-color: rgb(0, 0, 0);\n"
                                      "border-radius: 15%;\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "color: black;\n"
                                      'font: 14pt Calibri;\n'
                                      "border-color: black;")
        self.Python_btn.setObjectName("Python_btn")
        self.Aria_close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Aria_close_btn.setEnabled(True)
        self.Aria_close_btn.setGeometry(QtCore.QRect(500, 480, 261, 31))
        self.Aria_close_btn.setStyleSheet("background-color: white;\n"
                                          "gridline-color: rgb(0, 0, 0);\n"
                                          "border-radius: 15%;\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "color: black;\n"
                                          'font: 14pt Calibri;\n'
                                          "border-color: black;")
        self.Aria_close_btn.setObjectName("Aria_close_btn")
        self.Made_by_KZ = QtWidgets.QLabel(self.centralwidget)
        self.Made_by_KZ.setGeometry(QtCore.QRect(520, 520, 251, 25))
        self.Made_by_KZ.setStyleSheet("border-style: none;")
        self.Made_by_KZ.setObjectName("Made_by_KZ")

        MainWindow.setCentralWidget(self.centralwidget)
        self.Chat.setEnabled(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aria - Personal Voice Assistant"))
        self.Enter.setShortcut(_translate("MainWindow", "Return"))
        self.Microphone.setShortcut(_translate("MainWindow", "Down"))
        self.Chat.setHtml(_translate("MainWindow",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Aria.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#1d1d1d;\">Aria - Personal Voice Assistant</span></p></body></html>"))
        self.FAQ.setText(_translate("MainWindow",
                                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">FAQ</span></p></body></html>"))
        self.Make_a_note_btn.setText(_translate("MainWindow", "Make a note"))
        self.Check_notes_btn.setText(_translate("MainWindow", "Check notes"))
        self.Open_MS_Word_btn.setText(_translate("MainWindow", "Open Microsoft Word"))
        self.Show_random_picture_btn.setText(_translate("MainWindow", "Show random picture"))
        self.Open_donnu_btn.setText(_translate("MainWindow", "Open donnu.edu.ua"))
        self.Play_music_btn.setText(_translate("MainWindow", "Play music"))
        self.Play_video_btn.setText(_translate("MainWindow", "Play video"))
        self.Play_DL_WT_btn.setText(_translate("MainWindow", "Play Dua Lipa Want To"))
        self.Show_random_number_btn.setText(_translate("MainWindow", "Random number from 1 to 6"))
        self.Calculate_btn.setText(_translate("MainWindow", "(2 x 3) ^ 4"))
        self.Python_btn.setText(_translate("MainWindow", "What is Python?"))
        self.Aria_close_btn.setText(_translate("MainWindow", "Aria close"))
        self.Made_by_KZ.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#c3c3c3;\">Made by Kateryna Zakharova</span></p></body></html>"))
