from pages.pages_navigator import PageNavigator
from widgets.widgets_creator import WidgetsCreator
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QPushButton, QLabel, QFileDialog, QMainWindow, QWidget

class OperationPageWidgetsCreator(WidgetsCreator):

    def __init__(self, navigator: PageNavigator = None):
        super().__init__()
        self.navigator = navigator
        self._list_of_top_layout_widgets = []
        self._list_of_middle_layout_widgets = []
        self._list_of_bottom_layout_widgets = []
        self._list_of_top_left_layout_widgets = []
        self._list_of_top_right_layout_widgets = []
        self._list_of_top_right_top_layout_widgets = []
        self._list_of_top_right_bottom_layout_widgets = []
        self._reference_image = "./resource/face_placeholder.png"

    def set_reference_image(self, reference_image: str):
        self._reference_image = reference_image

    def get_reference_image(self):
        return self._reference_image

    def open_file_dialog(self, widget):
        file_name, _ = QFileDialog.getOpenFileName(widget, "Select a file", "", "All Files (*);;Image Files(.jpg)")
        if file_name and file_name.rfind('.') != -1:
            extension = file_name[file_name.rfind('.'):].lower()
            if extension == ".jpg" or extension == ".png":
                return file_name

    def examine_widgets(self, list_or_widget):
        if isinstance(list_or_widget, list):
            for item in list_or_widget:
                found_widget = self.examine_widgets(item)
                if found_widget is not None:
                    return found_widget
        else:
            if isinstance(list_or_widget, QLabel) and list_or_widget.objectName() == "source_face":
                return list_or_widget
        return None

    def _select_facial_image(self):
        label = self.examine_widgets(self._list_of_top_layout_widgets)

        if label:
            new_image = self.open_file_dialog(label)
            if new_image is not None:
                self.set_reference_image(new_image)
                pixmap = QPixmap(new_image)
                label.setPixmap(pixmap.scaled(label.width(), label.height()))

    def _select_file_path(self):
        print("Select Path")

    @staticmethod
    def _create_standard_button(layout_list: list, display, width, height, font_size, object_name: str,
                                icon=None, button_action=None):
        if icon:
            button = QPushButton(icon=QIcon(icon), text=display)
        else:
            button = QPushButton(display)
        button.setFixedSize(QSize(width, height))
        font = QFont()
        font.setPointSize(font_size)
        button.setFont(font)
        if button_action:
            button.clicked.connect(button_action)
        button.setObjectName(object_name)
        list.append(layout_list, button)

    @staticmethod
    def _create_standard_image(layout_list: list, display, width, height, object_name: str):
        label = QLabel()
        pixmap = QPixmap(display)
        resized_pixmap = pixmap.scaled(width, height)
        label.setPixmap(resized_pixmap)
        label.setFixedSize(width, height)
        label.setObjectName(object_name)
        list.append(layout_list, label)

    @staticmethod
    def _create_standard_label(layout_list: list, text, width, height, font_size, object_name: str):
        label = QLabel()
        label.setText(text)
        label.setFixedSize(width, height)
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        label.setFont(font)
        label.setObjectName(object_name)
        list.append(layout_list, label)

    def top_layout_widgets(self):
        self._create_standard_image(self._list_of_top_left_layout_widgets, self._reference_image,
                                    150, 150,
                                    "source_face")
        self._create_standard_label(self._list_of_top_right_top_layout_widgets, "No Path Selected",
                                    200, 50, 15, "path_name")
        self._create_standard_button(self._list_of_top_right_top_layout_widgets, "Select a Folder Path",
                                     120, 40, 10,
                                     "path_button", None, self._select_file_path)
        self._create_standard_label(self._list_of_top_right_bottom_layout_widgets, "0 images inside directory",
                                    200, 50, 15, "path_details")

    def middle_layout_widgets(self):
        self._create_standard_button(self._list_of_middle_layout_widgets, "Select Facial Image",
                                     120, 40, 10,
                                     "face_button", None, self._select_facial_image)
        self._create_standard_button(self._list_of_middle_layout_widgets, "Start",
                                     120, 40, 10,
                                     "execute_button", None, self._select_file_path)

    def bottom_layout_widgets(self):
        pass

    def get_top_layout_widgets(self):
        if not self._list_of_top_layout_widgets:
            self.top_layout_widgets()
        self._list_of_top_layout_widgets.append(self._list_of_top_left_layout_widgets)
        self._list_of_top_right_layout_widgets.append(self._list_of_top_right_top_layout_widgets)
        self._list_of_top_right_layout_widgets.append(self._list_of_top_right_bottom_layout_widgets)
        self._list_of_top_layout_widgets.append(self._list_of_top_right_layout_widgets)
        return self._list_of_top_layout_widgets

    def get_middle_layout_widgets(self):
        if not self._list_of_middle_layout_widgets:
            self.middle_layout_widgets()
        return self._list_of_middle_layout_widgets

    def get_bottom_layout_widgets(self):
        if not self._list_of_bottom_layout_widgets:
            self.bottom_layout_widgets()
        return self._list_of_bottom_layout_widgets
