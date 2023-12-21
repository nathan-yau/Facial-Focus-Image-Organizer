from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from sections.sections_creator import SectionsCreator


class OperationPageSectionsCreator(SectionsCreator):

    def add_widgets_to_layout(self, layout, widgets):
        for widget in widgets:
            if isinstance(widget, list):
                sub_layout = QVBoxLayout() if layout.__class__ == QHBoxLayout else QHBoxLayout()
                self.add_widgets_to_layout(sub_layout, widget)
                layout.addLayout(sub_layout)
            else:
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter)

    def _populate_section(self, outer_layout, widgets_function, object_name):
        sub_section = widgets_function()

        for index, section in enumerate(sub_section):
            inner_layout = QVBoxLayout()

            self.add_widgets_to_layout(inner_layout, section)

            inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            inner_layout.setContentsMargins(20, 20, 20, 20)
            inner_layout.setObjectName(object_name)
            outer_layout.addLayout(inner_layout)

        return outer_layout

    def create_sections(self, outer_layout, widget_creator):
        self._populate_section(outer_layout, widget_creator.get_top_layout_widgets, "top_layout")
