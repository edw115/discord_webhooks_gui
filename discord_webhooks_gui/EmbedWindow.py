# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Embed.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Embed(object):
    def setupUi(self, Embed):
        if not Embed.objectName():
            Embed.setObjectName(u"Embed")
        Embed.resize(780, 481)
        Embed.setMinimumSize(QSize(780, 481))
        Embed.setMaximumSize(QSize(780, 481))
        self.verticalLayoutWidget = QWidget(Embed)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 761, 461))
        self.mainVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(371, 141))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 51, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 71, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 80, 111, 16))
        self.authorInput = QLineEdit(self.groupBox)
        self.authorInput.setObjectName(u"authorInput")
        self.authorInput.setGeometry(QRect(10, 50, 351, 22))
        self.authorInput.setClearButtonEnabled(True)
        self.authorURL = QLineEdit(self.groupBox)
        self.authorURL.setObjectName(u"authorURL")
        self.authorURL.setGeometry(QRect(10, 100, 171, 22))
        self.authorURL.setClearButtonEnabled(True)
        self.authorIconURL = QLineEdit(self.groupBox)
        self.authorIconURL.setObjectName(u"authorIconURL")
        self.authorIconURL.setGeometry(QRect(190, 100, 171, 22))
        self.authorIconURL.setClearButtonEnabled(True)

        self.leftLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(371, 999))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 51, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 71, 16))
        self.embedTitle = QLineEdit(self.groupBox_2)
        self.embedTitle.setObjectName(u"embedTitle")
        self.embedTitle.setGeometry(QRect(10, 50, 351, 22))
        self.embedTitle.setClearButtonEnabled(True)
        self.embedDescription = QTextEdit(self.groupBox_2)
        self.embedDescription.setObjectName(u"embedDescription")
        self.embedDescription.setGeometry(QRect(10, 100, 351, 91))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 200, 57, 14))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 200, 31, 16))
        self.embedURL = QLineEdit(self.groupBox_2)
        self.embedURL.setObjectName(u"embedURL")
        self.embedURL.setEnabled(False)
        self.embedURL.setGeometry(QRect(10, 220, 221, 22))
        self.embedURL.setClearButtonEnabled(True)
        self.colorInput = QLineEdit(self.groupBox_2)
        self.colorInput.setObjectName(u"colorInput")
        self.colorInput.setEnabled(False)
        self.colorInput.setGeometry(QRect(240, 220, 41, 22))
        self.selectColorButton = QPushButton(self.groupBox_2)
        self.selectColorButton.setObjectName(u"selectColorButton")
        self.selectColorButton.setGeometry(QRect(290, 220, 71, 22))

        self.leftLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.leftLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.leftLayout)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(371, 121))
        self.addFieldButton = QPushButton(self.groupBox_3)
        self.addFieldButton.setObjectName(u"addFieldButton")
        self.addFieldButton.setGeometry(QRect(280, 30, 80, 22))
        self.addFieldButton.setCheckable(False)
        self.editFieldButton = QPushButton(self.groupBox_3)
        self.editFieldButton.setObjectName(u"editFieldButton")
        self.editFieldButton.setEnabled(False)
        self.editFieldButton.setGeometry(QRect(280, 60, 80, 22))
        self.deleteFieldButton = QPushButton(self.groupBox_3)
        self.deleteFieldButton.setObjectName(u"deleteFieldButton")
        self.deleteFieldButton.setEnabled(False)
        self.deleteFieldButton.setGeometry(QRect(280, 90, 80, 22))
        self.fieldsList = QListWidget(self.groupBox_3)
        self.fieldsList.setObjectName(u"fieldsList")
        self.fieldsList.setGeometry(QRect(10, 30, 261, 81))

        self.rightLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(371, 141))
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 30, 51, 16))
        self.imageInput = QLineEdit(self.groupBox_4)
        self.imageInput.setObjectName(u"imageInput")
        self.imageInput.setGeometry(QRect(10, 50, 351, 22))
        self.imageInput.setClearButtonEnabled(True)
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 71, 16))
        self.thumbnailInput = QLineEdit(self.groupBox_4)
        self.thumbnailInput.setObjectName(u"thumbnailInput")
        self.thumbnailInput.setGeometry(QRect(10, 100, 351, 22))
        self.thumbnailInput.setClearButtonEnabled(True)

        self.rightLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(371, 131))
        self.footerInput = QLineEdit(self.groupBox_5)
        self.footerInput.setObjectName(u"footerInput")
        self.footerInput.setGeometry(QRect(10, 50, 351, 22))
        self.footerInput.setClearButtonEnabled(True)
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 57, 14))
        self.timestampCheckbox = QCheckBox(self.groupBox_5)
        self.timestampCheckbox.setObjectName(u"timestampCheckbox")
        self.timestampCheckbox.setGeometry(QRect(20, 90, 91, 20))
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(160, 80, 101, 16))
        self.footerIconURL = QLineEdit(self.groupBox_5)
        self.footerIconURL.setObjectName(u"footerIconURL")
        self.footerIconURL.setEnabled(False)
        self.footerIconURL.setGeometry(QRect(160, 100, 201, 22))
        self.footerIconURL.setClearButtonEnabled(True)

        self.rightLayout.addWidget(self.groupBox_5)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.rightLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.rightLayout)


        self.mainVerticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.mainVerticalLayout.addWidget(self.line_2)

        self.addEmbed = QPushButton(self.verticalLayoutWidget)
        self.addEmbed.setObjectName(u"addEmbed")

        self.mainVerticalLayout.addWidget(self.addEmbed)


        self.retranslateUi(Embed)

        QMetaObject.connectSlotsByName(Embed)
    # setupUi

    def retranslateUi(self, Embed):
        Embed.setWindowTitle(QCoreApplication.translate("Embed", u"Embed", None))
        self.groupBox.setTitle(QCoreApplication.translate("Embed", u"Author", None))
        self.label.setText(QCoreApplication.translate("Embed", u"Author", None))
        self.label_2.setText(QCoreApplication.translate("Embed", u"Author URL", None))
        self.label_3.setText(QCoreApplication.translate("Embed", u"Author Icon URL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Embed", u"Body", None))
        self.label_4.setText(QCoreApplication.translate("Embed", u"Title", None))
        self.label_5.setText(QCoreApplication.translate("Embed", u"Description", None))
        self.label_6.setText(QCoreApplication.translate("Embed", u"Title URL", None))
        self.label_7.setText(QCoreApplication.translate("Embed", u"Color", None))
        self.selectColorButton.setText(QCoreApplication.translate("Embed", u"Select", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Embed", u"Fields", None))
        self.addFieldButton.setText(QCoreApplication.translate("Embed", u"Add", None))
        self.editFieldButton.setText(QCoreApplication.translate("Embed", u"Edit", None))
        self.deleteFieldButton.setText(QCoreApplication.translate("Embed", u"Delete", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Embed", u"Images", None))
        self.label_8.setText(QCoreApplication.translate("Embed", u"Image", None))
        self.label_9.setText(QCoreApplication.translate("Embed", u"Thumbnail", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Embed", u"Footer", None))
        self.label_10.setText(QCoreApplication.translate("Embed", u"Footer", None))
        self.timestampCheckbox.setText(QCoreApplication.translate("Embed", u"TimeStamp", None))
        self.label_11.setText(QCoreApplication.translate("Embed", u"Footer Icon URL", None))
        self.addEmbed.setText(QCoreApplication.translate("Embed", u"Add Embed", None))
    # retranslateUi

