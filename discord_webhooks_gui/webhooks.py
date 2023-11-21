import sys
import traceback
from core import webhook_validator, embed_dict_creation, embed_creation, field_dict_creation, send
from WebhookWindow import Ui_Webhook
from EmbedWindow import Ui_Embed
from FieldWindow import Ui_Field
from PySide6.QtGui import QScreen
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QObject, Signal
from PySide6.QtWidgets import (
    QApplication,
    QColorDialog,
    QPushButton,
    QWidget,
    QMainWindow,
    QFileDialog,
    QMessageBox,
)

def center_window(window):
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())

class WorkerSignals(QObject):
    """
    Worker Signals
    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class checkWebhookWorker(QRunnable):
    '''
    Worker that validates the webhook provided.
    '''
    def __init__(self, fn, *args, **kwargs):
        super(checkWebhookWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['callback'] = self.signals.progress
 

    @Slot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
        
class WebhookSenderWoker(QRunnable):
    '''
    Worker that send webhook
    '''
    def __init__(self,fn,*args, **kwargs):
        super(WebhookSenderWoker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class WebHookWindow(QMainWindow, Ui_Webhook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center_window(self)
        self.embeds = []
        self.avatar_value = None
        self.username_value = None
        self.webhook_request_status = False
        self.error = QMessageBox()
        self.error.setIcon(QMessageBox.Warning)
        self.success = QMessageBox()
        self.success.setIcon(QMessageBox.Information)
        self.embed_window = None
        self.threadpool = QThreadPool()
        self.webhookInput.textEdited.connect(self.check_webhook_worker)
        self.addEmbedButton.clicked.connect(self.add_embed_window)
        self.content.textChanged.connect(self.check_sending_conditions)
        self.embedsList.model().rowsInserted.connect(self.check_sending_conditions)
        self.embedsList.model().rowsRemoved.connect(self.check_sending_conditions)
        self.searchFileButton.clicked.connect(self.file_dialog)
        self.fileDirInput.textChanged.connect(self.check_sending_conditions)
        self.sendButton.clicked.connect(self.webhook_sender_worker)
        self.editEmbedButton.clicked.connect(self.edit_embed_window)
        self.embedsList.selectionModel().selectionChanged.connect(self.embed_selected)
        self.deleteEmbedButton.clicked.connect(self.delete_embed)
    
        self.show()
    
    def embed_selected(self, e):
        if len(self.embeds) > 0:
            if not self.editEmbedButton.isEnabled():
                self.editEmbedButton.setEnabled(True)
            if not self.deleteEmbedButton.isEnabled():
                self.deleteEmbedButton.setEnabled(True)
        else:
            self.editEmbedButton.setDisabled(True)
            self.deleteEmbedButton.setDisabled(True)

    def add_embed_window(self):
        self.embed_window = EmbedWindow(self)
        self.hide()
        self.embed_window.show()

    def edit_embed_window(self):
        self.edit_window = EditEmbedWindow(self)
        self.hide()
        self.edit_window.show()

    def delete_embed(self):
        selected_item = self.embedsList.selectedItems()[0]
        selected_index = self.embedsList.row(selected_item)
        self.embeds.pop(selected_index)
        self.embedsList.clear()
        self.embedsList.addItems(
            [f'Embed: {i+1}' for i in range(len(self.embeds))]
        )
        self.check_sending_conditions()

    def update_webhook_data(self, data):
        # print('update', data)
        pass

    def thread_complete(self):
        # print('THREAD COMPLETE')
        self.avatarInput.setText(self.avatar_value)
        self.usernameInput.setText(self.username_value)
        if self.webhook_request_status:
            self.success.setText(
                f'The Webhook URL is valid'
            )
            self.success.exec()
        else:
            if len(self.webhookInput.text()) > 0:
                self.error.setText(
                    f'The Webhook URL is invalid'
                )
                self.error.exec()
        self.avatar_value=None
        self.username_value=None
    
    def progress_fn(self, n):
        pass
        # print('done ', n)

    def check_webhook_worker(self):
        worker = checkWebhookWorker(self.check_webhook)
        worker.signals.result.connect(self.update_webhook_data)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    def check_webhook(self, callback):
        webhook_url = self.webhookInput.text()
        response = webhook_validator(webhook_url)
        if isinstance(response, str) or response['status_code'] != 200:
            self.webhook_request_status = False

        else:
            self.webhook_request_status = True
            self.avatar_value = response['avatar']
            self.username_value = response['username']
            callback.emit(response)
        self.check_sending_conditions()

    def file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", "c:\\")
        self.fileDirInput.setText(file_name[0])

    def check_sending_conditions(self):
        if self.webhook_request_status:
            if (len(self.content.toPlainText()) > 0 or 
                self.embedsList.count() > 0 or 
                len(self.fileDirInput.text()) > 0):
                self.sendButton.setEnabled(True)
            else:
                self.sendButton.setDisabled(True)
        else:
            self.sendButton.setDisabled(True)
    
    def webhook_sender_worker(self):
        sender_worker = WebhookSenderWoker(self.send_webhook)
        sender_worker.signals.result.connect(self.sender_update)
        sender_worker.signals.finished.connect(self.sender_finished)
        sender_worker.signals.progress.connect(self.sender_progress)
        self.sendButton.setDisabled(True)
        self.threadpool.start(sender_worker)

    def sender_progress(self, e):
        pass
    
    def sender_update(self,e):
        pass 

    def sender_finished(self):
        # print('Webhook has been sent')
        self.content.clear()
        self.fileDirInput.clear()
        self.check_sending_conditions()

    def send_webhook(self):
        # print('Sending Webhook')
        send(
            self.webhookInput.text(),
            self.avatarInput.text(),
            self.usernameInput.text(),
            self.content.toPlainText(),
            self.embeds,
            self.fileDirInput.text()
        )


class EmbedWindow(QWidget, Ui_Embed):
    def __init__(self, webhook_window):
        super().__init__()
        self.setupUi(self)
        center_window(self)
        self.fields = []
        self.embeds_colors = []
        self.nonCriticalError = QMessageBox()
        self.nonCriticalError.setIcon(QMessageBox.Warning)
        self.nonCriticalError.setWindowTitle('Error')
        self.webhook_window = webhook_window
        self.field_window = None
        self.fieldsList.selectionModel().selectionChanged.connect(self.field_selected)
        self.addFieldButton.clicked.connect(self.add_field_window)
        self.editFieldButton.clicked.connect(self.edit_field_window)
        self.addEmbed.clicked.connect(self.add_embed)
        self.selectColorButton.clicked.connect(self.color_dialog)
        self.deleteFieldButton.clicked.connect(self.delete_field)
        self.embedTitle.textChanged.connect(self.enable_title_url)
        self.footerInput.textChanged.connect(self.enable_footer_icon_url)

    def enable_footer_icon_url(self):
        if len(self.footerInput.text()) > 0:
            self.footerIconURL.setEnabled(True)
        else:
            self.footerIconURL.clear()
            self.footerIconURL.setDisabled(True)

    def enable_title_url(self):
        if len(self.embedTitle.text()) > 0:
            self.embedURL.setEnabled(True)
        else:
            self.embedURL.clear()
            self.embedURL.setDisabled(True)

    def field_selected(self,e):
        if len(self.fields)>0:
            if not self.editFieldButton.isEnabled():
                self.editFieldButton.setEnabled(True)
            if not self.deleteFieldButton.isEnabled():
                self.deleteFieldButton.setEnabled(True)
        else:
            self.editFieldButton.setDisabled(True)
            self.deleteFieldButton.setDisabled(True)

    def add_field_window(self):
        self.field_window = FieldWindow(self)
        self.hide()
        self.field_window.show()

    def edit_field_window(self):
        self.edit_field = EditFieldWindow(self)
        self.hide()
        self.edit_field.show()
    
    def delete_field(self):
        selected = self.fieldsList.selectedItems()[0]
        selected_index = self.fieldsList.row(selected)
        self.fields.pop(selected_index)
        self.fieldsList.clear()
        self.fieldsList.addItems([field['name'] for field in self.fields])
    
    def closeEvent(self,event):
        self.webhook_window.show()

    def color_dialog(self):
        color = QColorDialog.getColor(parent=self, title='Selec Embed Color')
        self.colorInput.setText(color.name())
        self.colorInput.setStyleSheet(
            f"background-color:{color.name()};color:{color.name()};"
        )

    def add_embed(self):

        if len(self.webhook_window.embeds)>=10:
            self.nonCriticalError.setText(
                "You have reached the limit of Embeds Allowed"
            )
            self.nonCriticalError.exec()
        else:
            if any(
                [
                    self.authorInput.text(),
                    self.embedTitle.text(),
                    self.embedDescription.toPlainText(),
                    self.fields,
                    self.imageInput.text(),
                    self.thumbnailInput.text(),
                    self.footerInput.text()
                ]
            ):
                embed_dict = embed_dict_creation(
                    self.authorInput.text(),
                    self.authorURL.text(),
                    self.authorIconURL.text(),
                    self.embedTitle.text(),
                    self.embedDescription.toPlainText(),
                    self.embedURL.text(),
                    self.colorInput.text(),
                    self.fields,
                    self.imageInput.text(),
                    self.thumbnailInput.text(),
                    self.footerInput.text(),
                    self.timestampCheckbox.isChecked(),
                    self.footerIconURL.text()
                )
                embed = embed_creation(embed_dict)
                self.webhook_window.embeds.append(embed)
                self.webhook_window.embedsList.clear()
                # self.webhook_window.embedsList.addItems([item.title for item in self.webhook_window.embeds])
                self.webhook_window.embedsList.addItems([f'Embed:{i+1}' for i in range(len(self.webhook_window.embeds))])
                self.close()
            else:
                self.nonCriticalError.setText(
                    "You must fill at least one of the following fields: Autor, Title, Description, Fields, Footer or Image."
                )
                self.nonCriticalError.exec()

class EditEmbedWindow(EmbedWindow):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.embed_list = self.main_window.embeds
        self.setWindowTitle('Edit Embed')
        self.editEmbed = QPushButton('Edit Embed')
        self.addEmbed.setVisible(False)
        self.editEmbed.clicked.connect(self.edit_embed)
        self.mainVerticalLayout.addWidget(self.editEmbed)
        selected_item = self.webhook_window.embedsList.selectedItems()[0]
        self.selected_index = self.webhook_window.embedsList.row(selected_item)
        self.embed = self.embed_list[self.selected_index]
        self.fields = self.embed.fields
        self.authorInput.setText(self.embed.author['name'])
        self.authorURL.setText(self.embed.author['url'])
        self.authorIconURL.setText(self.embed.author['icon_url'])
        self.embedTitle.setText(self.embed.title)
        self.embedDescription.setText(self.embed.description)
        self.embedURL.setText(self.embed.url)
        if self.embed.color is not None:
            color = "0x{:06x}".format(self.embed.color).replace('0x','#')
            self.colorInput.setText(color)
            self.colorInput.setStyleSheet(
                f"background-color:{color};color:{color};"
            )
        self.fieldsList.addItems([field['name'] for field in self.fields])
        self.imageInput.setText(self.embed.image['url'])
        self.thumbnailInput.setText(self.embed.thumbnail['url'])
        self.footerInput.setText(self.embed.footer['text'])
        if self.embed.timestamp:
            self.timestampCheckbox.setChecked(True)
        self.footerIconURL.setText(self.embed.footer['icon_url'])
        self.fieldsList.selectionModel().selectionChanged.connect(self.field_selected)

    def field_selected(self,e):
        if len(self.embed.fields)>0:
            if not self.editFieldButton.isEnabled():
                self.editFieldButton.setEnabled(True)
            if not self.deleteFieldButton.isEnabled():
                self.deleteFieldButton.setEnabled(True)
        else:
            self.editFieldButton.setDisabled(True)
            self.deleteFieldButton.setDisabled(True)

    def edit_embed(self):
        if any(
                [
                    self.authorInput.text(),
                    self.embedTitle.text(),
                    self.embedDescription.toPlainText(),
                    self.fields,
                    self.imageInput.text(),
                    self.thumbnailInput.text(),
                    self.footerInput.text()
                ]
            ):
            embed_dict = embed_dict_creation(
                self.authorInput.text(),
                self.authorURL.text(),
                self.authorIconURL.text(),
                self.embedTitle.text(),
                self.embedDescription.toPlainText(),
                self.embedURL.text(),
                self.colorInput.text(),
                self.fields,
                self.imageInput.text(),
                self.thumbnailInput.text(),
                self.footerInput.text(),
                self.timestampCheckbox.isChecked(),
                self.footerIconURL.text()
            )
            embed = embed_creation(embed_dict)
            self.webhook_window.embeds.pop(self.selected_index)
            self.webhook_window.embeds.insert(self.selected_index, embed)
            self.webhook_window.embedsList.clear()
            self.webhook_window.embedsList.addItems(
              [f"Embed: {i+1}" for i in range(len(self.webhook_window.embeds))]  
            )
            self.close()
        else:
            self.nonCriticalError.setText(
                "You must fill at least one of the following fields: Autor, Title, Description, Fields, Footer or Image."
            )
            self.nonCriticalError.exec()

    def closeEvent(self, event):
        self.main_window.show()

class FieldWindow(QWidget, Ui_Field):
    def __init__(self, embed_window):
        super().__init__()
        self.setupUi(self)
        center_window(self)
        self.embed_window = embed_window
        self.fieldErrorMessage = QMessageBox()
        self.fieldErrorMessage.setIcon(QMessageBox.Warning)
        self.fieldErrorMessage.setWindowTitle('Error')

        self.addField.clicked.connect(self.add_field)
    
    def add_field(self):
        if len(self.embed_window.fields)>=25:
            self.fieldErrorMessage.setText(
                "You have been reached the limit amount of fields per Embed"
            ) 
            self.fieldErrorMessage.exec()
        else:
            if all([
                self.nameInput.text(),
                self.valueInput.text()
            ]):
                field_dict = field_dict_creation(
                    self.nameInput.text(),
                    self.valueInput.text(),
                    self.inlineCheckbox.isCheckable()
                )
                self.embed_window.fields.append(
                    field_dict
                ) 
                self.embed_window.fieldsList.clear()
                self.embed_window.fieldsList.addItems([i['name'] for i in self.embed_window.fields])
                self.close()
            else:
                self.fieldErrorMessage.setText(
                    "You mus fill name and value fields"
                ) 
                self.fieldErrorMessage.exec() 

    def closeEvent(self, event):
        self.embed_window.show()

class EditFieldWindow(FieldWindow):
    def __init__(self, embed_window):
        super().__init__(embed_window)
        self.embed_window = embed_window
        self.setWindowTitle('Edit Field')
        self.editField = QPushButton('Edit Field')
        selected_item = self.embed_window.fieldsList.selectedItems()[0]
        self.selected_index = self.embed_window.fieldsList.row(selected_item)
        field = self.embed_window.fields[self.selected_index]
        self.nameInput.setText(field['name'])
        self.valueInput.setText(field['value'])
        self.inlineCheckbox.setChecked(field['inline'])
        self.addField.setVisible(False)
        self.verticalLayout.addWidget(self.editField)
        self.editField.clicked.connect(self.edit_field)

    def edit_field(self):
        item = {
            'name':self.nameInput.text(),
            'value':self.valueInput.text(),
            'inline':self.inlineCheckbox.isChecked()
        }
        self.embed_window.fields.pop(self.selected_index)
        self.embed_window.fields.insert(self.selected_index, item)
        self.embed_window.fieldsList.clear()
        self.embed_window.fieldsList.addItems(
            [item['name'] for item in self.embed_window.fields]
        )
        self.close()

    def closeEvent(self, event):
        self.embed_window.show()


app = QApplication(sys.argv)
app.setStyle('Fusion')
main_window = WebHookWindow()

app.exec()