# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Field.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Field(object):
    def setupUi(self, Field):
        if not Field.objectName():
            Field.setObjectName(u"Field")
        Field.resize(281, 213)
        Field.setMinimumSize(QSize(281, 213))
        Field.setMaximumSize(QSize(281, 213))
        self.verticalLayoutWidget = QWidget(Field)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 261, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 57, 14))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 57, 14))
        self.inlineCheckbox = QCheckBox(self.groupBox)
        self.inlineCheckbox.setObjectName(u"inlineCheckbox")
        self.inlineCheckbox.setGeometry(QRect(10, 130, 85, 20))
        self.inlineCheckbox.setChecked(True)
        self.nameInput = QLineEdit(self.groupBox)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(10, 40, 241, 22))
        self.nameInput.setMaxLength(256)
        self.nameInput.setClearButtonEnabled(True)
        self.valueInput = QLineEdit(self.groupBox)
        self.valueInput.setObjectName(u"valueInput")
        self.valueInput.setGeometry(QRect(10, 90, 241, 22))
        self.valueInput.setMaxLength(1024)
        self.valueInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.groupBox)

        self.addField = QPushButton(self.verticalLayoutWidget)
        self.addField.setObjectName(u"addField")

        self.verticalLayout.addWidget(self.addField)


        self.retranslateUi(Field)

        QMetaObject.connectSlotsByName(Field)
    # setupUi

    def retranslateUi(self, Field):
        Field.setWindowTitle(QCoreApplication.translate("Field", u"Field", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Field", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Field", u"Value", None))
        self.inlineCheckbox.setText(QCoreApplication.translate("Field", u"Inline", None))
        self.addField.setText(QCoreApplication.translate("Field", u"Add Field", None))
    # retranslateUi

