# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WebHook.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Webhook(object):
    def setupUi(self, Webhook):
        if not Webhook.objectName():
            Webhook.setObjectName(u"Webhook")
        Webhook.resize(432, 521)
        Webhook.setMinimumSize(QSize(432, 521))
        Webhook.setMaximumSize(QSize(432, 521))
        self.centralwidget = QWidget(Webhook)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 411, 471))
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(461, 471))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 101, 16))
        self.webhookInput = QLineEdit(self.groupBox)
        self.webhookInput.setObjectName(u"webhookInput")
        self.webhookInput.setGeometry(QRect(10, 40, 391, 22))
        self.webhookInput.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 61, 16))
        self.avatarInput = QLineEdit(self.groupBox)
        self.avatarInput.setObjectName(u"avatarInput")
        self.avatarInput.setGeometry(QRect(10, 90, 391, 22))
        self.avatarInput.setClearButtonEnabled(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 71, 16))
        self.usernameInput = QLineEdit(self.groupBox)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(10, 140, 391, 22))
        self.usernameInput.setMaximumSize(QSize(441, 16777215))
        self.usernameInput.setClearButtonEnabled(True)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 61, 16))
        self.content = QTextEdit(self.groupBox)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(10, 190, 391, 101))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 300, 61, 16))
        self.addEmbedButton = QPushButton(self.groupBox)
        self.addEmbedButton.setObjectName(u"addEmbedButton")
        self.addEmbedButton.setGeometry(QRect(330, 320, 71, 22))
        self.editEmbedButton = QPushButton(self.groupBox)
        self.editEmbedButton.setObjectName(u"editEmbedButton")
        self.editEmbedButton.setEnabled(False)
        self.editEmbedButton.setGeometry(QRect(330, 350, 71, 22))
        self.deleteEmbedButton = QPushButton(self.groupBox)
        self.deleteEmbedButton.setObjectName(u"deleteEmbedButton")
        self.deleteEmbedButton.setEnabled(False)
        self.deleteEmbedButton.setGeometry(QRect(330, 380, 71, 22))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 410, 51, 16))
        self.searchFileButton = QPushButton(self.groupBox)
        self.searchFileButton.setObjectName(u"searchFileButton")
        self.searchFileButton.setGeometry(QRect(330, 430, 71, 22))
        self.embedsList = QListWidget(self.groupBox)
        self.embedsList.setObjectName(u"embedsList")
        self.embedsList.setGeometry(QRect(10, 320, 311, 81))
        self.fileDirInput = QLineEdit(self.groupBox)
        self.fileDirInput.setObjectName(u"fileDirInput")
        self.fileDirInput.setEnabled(False)
        self.fileDirInput.setGeometry(QRect(10, 430, 311, 22))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setEnabled(False)
        self.sendButton.setGeometry(QRect(10, 490, 411, 21))
        Webhook.setCentralWidget(self.centralwidget)

        self.retranslateUi(Webhook)

        QMetaObject.connectSlotsByName(Webhook)
    # setupUi

    def retranslateUi(self, Webhook):
        Webhook.setWindowTitle(QCoreApplication.translate("Webhook", u"Discord Webhooks", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Webhook", u"WebHook URL", None))
        self.label_2.setText(QCoreApplication.translate("Webhook", u"Avatar", None))
        self.label_3.setText(QCoreApplication.translate("Webhook", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Webhook", u"Content", None))
        self.label_5.setText(QCoreApplication.translate("Webhook", u"Embeds", None))
        self.addEmbedButton.setText(QCoreApplication.translate("Webhook", u"Add", None))
        self.editEmbedButton.setText(QCoreApplication.translate("Webhook", u"Edit", None))
        self.deleteEmbedButton.setText(QCoreApplication.translate("Webhook", u"Delete", None))
        self.label_6.setText(QCoreApplication.translate("Webhook", u"File", None))
        self.searchFileButton.setText(QCoreApplication.translate("Webhook", u"Search", None))
        self.sendButton.setText(QCoreApplication.translate("Webhook", u"Send", None))
    # retranslateUi

